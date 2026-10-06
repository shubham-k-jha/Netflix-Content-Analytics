"""Single authoritative rebuild command."""
from __future__ import annotations
import json, sqlite3, subprocess, sys
import pandas as pd
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from src.pipeline import build, write_manifest, sha256_file
from src.advanced import run_advanced


def run_sql():
    db=ROOT/'data/processed/netflix_analytics.db'
    con=sqlite3.connect(db); results=[]
    try:
        for path in sorted((ROOT/'sql').glob('*.sql')):
            sql=path.read_text(encoding='utf-8')
            try:
                cur=con.execute(sql); rows=cur.fetchall(); cols=[d[0] for d in cur.description] if cur.description else []
                results.append({'file':str(path.relative_to(ROOT)),'status':'PASS','rows':len(rows),'columns':cols})
            except Exception as exc:
                results.append({'file':str(path.relative_to(ROOT)),'status':'FAIL','error':str(exc)})
                raise RuntimeError(f'SQL failed: {path.name}: {exc}') from exc
    finally: con.close()
    report={'sql_files':len(results),'passed':sum(x['status']=='PASS' for x in results),'results':results}
    (ROOT/'reports/sql_execution_report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    return report

summary,*_=build()
subprocess.run([sys.executable,'-m','src.analysis'],cwd=ROOT,check=True)
# v8 advanced analytics are generated after the base analytical marts exist.
g=pd.read_csv(ROOT/'data/processed/global_analytics.csv',parse_dates=['week','release_date','prev_week','next_week'])
c=pd.read_csv(ROOT/'data/processed/country_analytics.csv',parse_dates=['week','release_date'])
m=pd.read_csv(ROOT/'data/processed/title_performance_mart.csv',parse_dates=['first_week','last_week','release_date'])
t=pd.read_csv(ROOT/'data/processed/tmdb_metadata.csv',parse_dates=['release_date'])
st=pd.read_csv(ROOT/'reports/statistical_results.csv')
run_advanced(g,c,m,t,st)
sql=run_sql()
# Add SQL report and final outputs to provenance after all build stages.
from src.pipeline import write_manifest
write_manifest(summary)
print(json.dumps({'summary':summary,'sql':sql},indent=2,default=str))
