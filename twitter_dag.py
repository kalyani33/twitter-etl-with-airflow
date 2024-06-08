
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime,timedelta
from twitter_etl import run_twitter_etl 

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': 'airflow@example.com',
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'start_date': datetime(2024, 1, 1),
}
 
dag = DAG('twitter_dag', default_args=default_args)
 
run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=run_twitter_etl,
    dag=dag
)
