import airflow
import logging
from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago


#Datos del job
job_name = 'EjemploETL'
job_version = '0.1'
contexto =  " --context=PROD"
parametros = " --context_param LOG=AIRFLOW"

#Definición de ruta
#Cambiar pwd en script.sh
airflow_home = '/opt/airflow'
talend_job = airflow_home + '/exec/' + job_name + '_' + job_version + '/' + job_name + '/' + job_name + '_run.sh'
script_job = talend_job + contexto + parametros

default_args = {
    'owner': 'TEST',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

def imprimir():
    logging.info(script_job)

with DAG(
    'example_talend',
    template_searchpath="/",
    default_args=default_args,
    description='A simple tutorial DAG',
    start_date=days_ago(0),
    schedule_interval=timedelta(days=3),
    tags=['example'],
) as dag:
    imprimir_task = PythonOperator(
        task_id="imprimir", 
        python_callable=imprimir
    )
    ejecutar_task = BashOperator(
        task_id="ejecutarEtl",
        bash_command=script_job,
    )
    
    imprimir_task >> ejecutar_task
