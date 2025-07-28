from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

def push_message(**context):
    return "Hello from PythonOperator using XCom!"

with DAG(
    dag_id="xcom_demo_dag",
    start_date=datetime(2025, 6, 1),
    schedule=None,
    catchup=False,
    tags=["example"],
) as dag:

    push_task = PythonOperator(
        task_id="push_message",
        python_callable=push_message,
    )

    pull_task = BashOperator(
        task_id="pull_message",
        bash_command='echo "{{ ti.xcom_pull(task_ids=\'push_message\') }}"',
    )

    push_task >> pull_task
