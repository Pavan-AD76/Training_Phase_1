from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime


def fetch_config():
    api_endpoint = Variable.get("api_endpoint")
    print(f"Using API endpoint: {api_endpoint}")


with DAG(
    dag_id='variable_demo_dag',
    start_date=datetime(2023, 1, 1),
    schedule="*/5 * * * *",  
    catchup=False,
) as dag:
    
    print_api_url = PythonOperator(
        task_id='print_api_endpoint',
        python_callable=fetch_config
    )
