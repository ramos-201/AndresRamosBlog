from starlette.testclient import TestClient

from src.app import app


def test_connection_with_app_successful():
    client = TestClient(app)
    response = client.get('/hw')
    assert response.status_code == 200
    assert response.content == b'{"hello":"world"}'
