from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'TEST',
    'retries': 0,
    'retry_delay': timedelta(minutes=1)
}

def imprimir(ti):
    resultado = ti.xcom_pull(task_ids='select_db')
    print(resultado)

with DAG(
    dag_id='example_mysql_conn',
    default_args=default_args,
    start_date=datetime(2023,11,13),
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    task1 = MySqlOperator(
        task_id='select_db',
        mysql_conn_id='PPS_GESTION',
        sql="""
            SELECT 
                Activo,
                Categoria,
                Sexo
            FROM GESTION_PADRON_SANITARIO_SOCIAL gpss 
            LIMIT 10
        """
    )

    task2 = PythonOperator(
        task_id='print',
        python_callable=imprimir
    )

    task1 >> task2
