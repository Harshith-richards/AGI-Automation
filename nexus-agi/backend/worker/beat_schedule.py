from .celery_app import celery_app

celery_app.conf.beat_schedule = {
    'nightly-improvement-loop': {
        'task': 'backend.worker.task_worker.execute_task',
        'schedule': 86400.0,
        'args': ('Run nightly self-improvement audit',),
    }
}
