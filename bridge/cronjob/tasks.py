from celery import shared_task
from .etl_tasks import run_etl

@shared_task
def run_etl_task():
    run_etl()
