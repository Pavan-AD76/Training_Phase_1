from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests

def print_welcome():
    print('Welcome to Airflow!')

def print_date():
    print('Today is {}'.format(datetime.today().date()))

def print_random_quote():
    try:
        response = requests.get('https://api.quotable.io/random', timeout=10)
        response.raise_for_status()
        quote = response.json().get('content', 'No quote found.')
        print(f'Quote of the day: "{quote}"')
    except Exception as e:
        print(f"Failed to fetch quote: {e}")

default_args = {
    'owner': 'airflow',
    'start_date': datetime.now() - timedelta(days=1),
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

dag = DAG(
    dag_id='welcome_dag',
    default_args=default_args,
    schedule='0 23 * * *',  # updated for Airflow 2.9+
    catchup=False,
)

print_welcome_task = PythonOperator(
    task_id='print_welcome',
    python_callable=print_welcome,
    dag=dag
)

print_date_task = PythonOperator(
    task_id='print_date',
    python_callable=print_date,
    dag=dag
)

print_random_quote_task = PythonOperator(
    task_id='print_random_quote',
    python_callable=print_random_quote,
    dag=dag
)

print_welcome_task >> print_date_task >> print_random_quote_task
