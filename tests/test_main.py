from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_home_returns_json():
    response = client.get("/")
    assert response.headers["content-type"].startswith("application/json")


def test_invalid_endpoint():
    response = client.get("/invalid-endpoint")
    assert response.status_code == 404
