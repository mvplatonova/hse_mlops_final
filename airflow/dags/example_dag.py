from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG("test_dag", start_date=datetime(2024, 1, 1), schedule=None, catchup=False) as dag:
    PythonOperator(task_id="hello", python_callable=lambda: print("it works"))
