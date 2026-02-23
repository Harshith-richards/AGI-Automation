from celery import Celery
from ..config import get_settings

settings = get_settings()
celery_app = Celery('nexus', broker=settings.celery_broker_url, backend=settings.celery_result_backend)
celery_app.conf.task_routes = {'backend.worker.task_worker.execute_task': {'queue': 'tasks'}}
