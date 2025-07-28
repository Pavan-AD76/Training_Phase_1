from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime


def run_python_task():
    print("Task executed successfully")


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

    python_task = PythonOperator(
        task_id='run_python',
        python_callable=run_python_task
    )

    hello_task >> python_task  