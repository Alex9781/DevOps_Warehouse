import pytest
from app.app import app as _app

@pytest.fixture()
def app():
    app = _app
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

def test_index(client):
    response = client.get("/")
    assert response.status_code == 302

def test_login(client):
    response = client.get("/auth/login")
    assert response.status_code == 200

def test_login_post(client):
    response = client.post("/auth/login", data={
        "login": "test_user",
        "password": "qwerty",
    })
    assert response.status_code == 302

def test_login_post_incorrect(client):
    response = client.post("/auth/login", data={
        "login": "test_user",
        "password": "12345",
    })
    assert response.status_code == 200

