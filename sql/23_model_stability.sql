SELECT cutoff_fraction, cutoff_week, model, train_rows, test_rows, mae, rmse, r2
FROM model_stability ORDER BY cutoff_fraction, model;
