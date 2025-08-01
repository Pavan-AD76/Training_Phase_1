from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='hello_airflow_dag',
    start_date=datetime(2023, 1, 1),
    schedule=None, 
    catchup=False,
) as dag:
    
    hello_task = BashOperator(
        task_id='say_hello',
        bash_command='echo "Hello AirFlow!"'
    )
