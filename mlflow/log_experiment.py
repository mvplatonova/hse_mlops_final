import mlflow

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("mlflow-experiment")

with mlflow.start_run():
    mlflow.log_param("model", "logreg")
    mlflow.log_metric("acc", 0.97)
