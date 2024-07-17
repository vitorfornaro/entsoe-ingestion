from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Função Python que será executada pela DAG
def hello_world():
    print("Hello, world!")

# Definição padrão dos argumentos
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 7, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Criação da DAG
dag = DAG(
    'minha_primeira_dag',
    default_args=default_args,
    description='Uma DAG simples que imprime Hello, world!',
    schedule_interval=timedelta(days=1),
)

# Definição da tarefa que executa a função hello_world
hello_world_task = PythonOperator(
    task_id='minha_primeira_dag',
    python_callable=hello_world,
    dag=dag,
)

# Debug log para confirmar que a DAG está sendo lida
if __name__ == "__main__":
    print("DAG carregada com sucesso!")