from fastapi import APIRouter
from ...tools.registry import registry, ToolSpec

router = APIRouter(prefix='/api', tags=['tools'])


@router.get('/tools')
def list_tools():
    return registry.list()


@router.post('/tools')
def register_tool(payload: dict):
    name = payload['name']
    registry.register(ToolSpec(name=name, description=payload.get('description','custom tool'), schema=payload.get('schema',{}), handler=lambda x: x))
    return {'registered': name}


@router.post('/tools/{name}/test')
def test_tool(name: str, payload: dict):
    return registry.execute(name, payload)
