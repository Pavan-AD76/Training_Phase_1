from airflow import DAG
from datetime import datetime  
from greet_plugin import GreetOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id="greet_dag",
    default_args=default_args,
    description="A simple greet DAG",
    schedule="@daily",  
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:


    greet = GreetOperator(
        task_id='greet_task',
        name='Nithya'
    )
