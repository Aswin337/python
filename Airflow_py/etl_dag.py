from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime,timedelta

default_args={
    "owner":"airflow",
    "depends_on_past":False,
    "email_on_failure":False,
    "email_on_retry":False,
    "retries":1,
    "retry_delay":timedelta(minutes=7)
}

dag=DAG(
    "mysql_etl_dag",
    default_args=default_args,
    description="A simple Mysql ETL DAG",
    schedule_interval=timedelta(minutes=3),
    start_date=datetime(2025,9,27),
    catchup=False
)

run_etl=BashOperator (
    task_id="run_etl",
    bash_command="bash /home/aswinkumar/wrapper_script.sh ",
    dag=dag,
)