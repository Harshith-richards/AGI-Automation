from fastapi import APIRouter

router = APIRouter(prefix='/api', tags=['memory'])
MEM: list[dict] = []


@router.get('/memory/search')
def search_memory(q: str):
    return [m for m in MEM if q.lower() in str(m).lower()]


@router.post('/memory')
def save_memory(payload: dict):
    MEM.append(payload)
    return payload


@router.delete('/memory/{mid}')
def delete_memory(mid: int):
    if 0 <= mid < len(MEM):
        MEM.pop(mid)
    return {'deleted': mid}
