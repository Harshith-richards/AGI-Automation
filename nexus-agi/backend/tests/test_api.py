from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_health():
    r = client.get('/health')
    assert r.status_code == 200


def test_tools_available():
    r = client.get('/api/tools')
    assert r.status_code == 200
    assert isinstance(r.json(), list)
