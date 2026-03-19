from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from weather_etl.extract import extract_weather
from weather_etl.transform import transform_weather
from weather_etl.load import load_weather

default_args = {
    "owner": "kelash",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

def run_etl():
    raw_data = extract_weather()
    df = transform_weather(raw_data)
    load_weather(df)

with DAG(
    dag_id="weather_etl_pipeline",
    default_args=default_args,
    description="ETL pipeline for weather data",
    schedule_interval="@hourly",
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    run_pipeline = PythonOperator(
        task_id="run_weather_etl",
        python_callable=run_etl
    )
