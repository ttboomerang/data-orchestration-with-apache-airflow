from airflow.sdk import DAG
from airflow.utils import timezone
from airflow.providers.standard.operators.empty import EmptyOperator
import logging

with DAG(
    "my_first_dag",
    start_date = timezone.datetime(2025, 10, 2),
    schedule = None,

):
    t1 = EmptyOperator(task_id = "t1")
    t2 = EmptyOperator(task_id = "t2")
    t3 = EmptyOperator(task_id = "t3")
    t4 = EmptyOperator(task_id = "t4")
    t5 = EmptyOperator(task_id = "t5")
    t6 = EmptyOperator(task_id = "t6")
    t7 = EmptyOperator(task_id = "t7")
    t8 = EmptyOperator(task_id = "t8")
    t9 = EmptyOperator(task_id = "t9")

    #Dependencies
    t1 >> [t2, t5]
    t2 >> [t3, t6]
    t3 >> t4 >> t9
    t5 >> [t6, t7]
    [t6, t7] >> t8 >> t9