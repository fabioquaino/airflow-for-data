from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "TEST",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Add your code to train your model here
with DAG("example_dummy", default_args=default_args, schedule="0 4 * * *"):
    dummy_task = DummyOperator(
        task_id="dummy_task",
    )
