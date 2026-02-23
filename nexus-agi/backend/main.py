from fastapi import FastAPI
from .api.routes.tasks import router as tasks_router
from .api.routes.agents import router as agents_router
from .api.routes.memory import router as memory_router
from .api.routes.tools import router as tools_router
from .api.routes.metrics import router as metrics_router
from .api.websockets import router as ws_router
from .database import Base, engine
from .tools import search_tools, code_tools, web_tools, data_tools, file_tools, comm_tools, memory_tools

app = FastAPI(title='NEXUS-AGI API')
Base.metadata.create_all(bind=engine)

search_tools.register_tools()
code_tools.register_tools()
web_tools.register_tools()
data_tools.register_tools()
file_tools.register_tools()
comm_tools.register_tools()
memory_tools.register_tools()

app.include_router(tasks_router)
app.include_router(agents_router)
app.include_router(memory_router)
app.include_router(tools_router)
app.include_router(metrics_router)
app.include_router(ws_router)


@app.get('/health')
def health():
    return {'status': 'ok'}
