# Weather ETL Pipeline 🌤️

An automated data engineering pipeline that extracts real-time weather data
for Pakistani cities, transforms it, and loads it into PostgreSQL —
scheduled and orchestrated using Apache Airflow.

## Architecture
OpenWeatherMap API → Extract → Transform → Load → PostgreSQL
                                   ↑
                            Apache Airflow
                          (Hourly Schedule)

## Tech Stack
- Python 3.10
- Apache Airflow 2.9
- PostgreSQL 14
- Pandas
- psycopg2

## Pipeline Structure
- extract.py — Fetches live weather data from API
- transform.py — Cleans raw JSON into structured DataFrame
- load.py — Inserts data into PostgreSQL
- weather_dag.py — Airflow DAG orchestrating the full pipeline

## What It Does
- Extracts live weather data for Karachi, Lahore and Islamabad
- Transforms raw API response into structured rows
- Loads data into PostgreSQL automatically every hour
- Tracks temperature, humidity, wind speed and weather conditions

## Author
Kelash Kumar — Data Engineering Aspirant
LinkedIn: https://linkedin.com/in/kelashkumar-iba
