from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ...agents.orchestrator import Orchestrator

router = APIRouter(prefix='/api', tags=['tasks'])
TASKS: dict[str, dict] = {}


class TaskCreate(BaseModel):
    id: str
    goal: str


@router.post('/task')
async def create_task(req: TaskCreate):
    orchestrator = Orchestrator()
    result = await orchestrator.execute(req.goal)
    TASKS[req.id] = result
    return result


@router.get('/task/{task_id}')
def get_task(task_id: str):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail='task not found')
    return TASKS[task_id]


@router.delete('/task/{task_id}')
def cancel_task(task_id: str):
    if task_id in TASKS:
        TASKS[task_id]['status'] = 'cancelled'
    return {'task_id': task_id, 'status': 'cancelled'}


@router.get('/tasks')
def list_tasks():
    return list(TASKS.values())


@router.post('/task/{task_id}/pause')
def pause_task(task_id: str):
    if task_id in TASKS:
        TASKS[task_id]['status'] = 'paused'
    return {'task_id': task_id, 'status': 'paused'}


@router.post('/task/{task_id}/resume')
def resume_task(task_id: str):
    if task_id in TASKS:
        TASKS[task_id]['status'] = 'running'
    return {'task_id': task_id, 'status': 'running'}


@router.post('/task/{task_id}/approve')
def approve_task(task_id: str):
    return {'task_id': task_id, 'checkpoint': 'approved'}
