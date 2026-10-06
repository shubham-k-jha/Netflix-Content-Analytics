PYTHON ?= python3

.PHONY: build validate analysis test dashboard verify clean

build:
	$(PYTHON) scripts/run_pipeline.py

validate:
	$(PYTHON) -m src.pipeline

analysis:
	$(PYTHON) -m src.analysis

test:
	$(PYTHON) -m pytest

dashboard:
	$(PYTHON) -m streamlit run dashboard/app.py

verify:
	$(PYTHON) scripts/run_pipeline.py
	$(PYTHON) -m pytest

clean:
	rm -rf data/processed reports __pycache__ src/__pycache__ tests/__pycache__ dashboard/__pycache__
