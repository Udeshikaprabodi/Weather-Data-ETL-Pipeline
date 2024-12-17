from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.extract_data import extract_data
from scripts.transform_data import transform_data
from scripts.load_data import load_data

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 1,
    'start_date': datetime(2024, 12, 17),
}

# Define the DAG
with DAG(
    'weather_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )

    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
    )

    extract_task >> transform_task >> load_task
