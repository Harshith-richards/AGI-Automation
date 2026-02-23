from fastapi import APIRouter, WebSocket

router = APIRouter()


@router.websocket('/ws/task/{task_id}')
async def task_stream(websocket: WebSocket, task_id: str):
    await websocket.accept()
    await websocket.send_json({'task_id': task_id, 'event': 'connected'})
    await websocket.close()
