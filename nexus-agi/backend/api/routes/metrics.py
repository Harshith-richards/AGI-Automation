from fastapi import APIRouter

router = APIRouter(prefix='/api', tags=['metrics'])


@router.get('/metrics')
def metrics():
    return {'tasks_per_hour': 0, 'success_rate': 1.0, 'token_usage': 0, 'cost': 0}
