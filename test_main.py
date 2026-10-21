from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_endpoints():
    assert client.get("/").json() == {"message": "FastAPI is running on Porter"}
    assert client.get("/healthz").json() == {"status": "ok"}
    assert client.get("/hello/porter").json() == {"message": "Hello, porter!"}
