from fastapi import APIRouter

router = APIRouter(prefix='/api', tags=['agents'])


@router.get('/agents')
def list_agents():
    names = ['researcher','coder','analyst','browser','filesystem','communicator','memory_agent','critic','tool_builder','scheduler']
    return [{'name': n, 'status': 'ready'} for n in names]


@router.get('/agents/{name}/logs')
def agent_logs(name: str):
    return {'agent': name, 'logs': []}
