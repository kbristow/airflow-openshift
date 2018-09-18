from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import uuid

args = {
    "owner": "airflow",
    'start_date': datetime(2018, 10, 18),
    "provide_context": True
}

dag = DAG(
    "run_and_report",
    schedule_interval=None,
    default_args=args)

def get_and_store_date(**context):
    #Return statements are automatically pushed into xcom
    return context["ds"]

def generate_uuid(**context):
    new_uuid = uuid.uuid4()
    context["ti"].xcom_push(key="uuid_str", value=str(new_uuid))
    context["ti"].xcom_push(key="uuid_hex", value=new_uuid.hex)

def print_report(**context):
    uuid_str = context["ti"].xcom_pull(key="uuid_str", task_ids="uuid")
    uuid_hex = context["ti"].xcom_pull(key="uuid_hex", task_ids="uuid")
    run_date = context["ti"].xcom_pull(key=None, task_ids="date")
    echo = context["ti"].xcom_pull(key=None, task_ids="echo")

    print(f"UUID String Representation: {uuid_str}")
    print(f"UUID Hex Representation: {uuid_hex}")
    print(f"Date Task Run Date: {run_date}")
    print(f"Echo Task Output: {echo}")


date_task = PythonOperator(
    task_id="date", dag=dag, python_callable=get_and_store_date)

uuid_task = PythonOperator(
    task_id="uuid", dag=dag, python_callable=generate_uuid)

echo_task = BashOperator(
    task_id="echo", dag=dag, bash_command="echo hello", xcom_push=True)

report_task = PythonOperator(
    task_id="report", dag=dag, python_callable=print_report)

report_task.set_upstream([date_task, uuid_task, echo_task])