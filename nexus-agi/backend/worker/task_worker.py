import asyncio
from .celery_app import celery_app
from ..agents.orchestrator import Orchestrator


@celery_app.task(name='backend.worker.task_worker.execute_task')
def execute_task(goal: str):
    orchestrator = Orchestrator()
    return asyncio.run(orchestrator.execute(goal))
