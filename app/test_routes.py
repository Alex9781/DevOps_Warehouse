import pytest
from app.app import create_app

@pytest.fixture()
def app():
    from dotenv import load_dotenv
    load_dotenv()
    app = create_app("config.py")
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

def test_index(client):    # Тест на переадресацию с корневой страницы
    response = client.get("/")
    assert response.status_code == 302

def test_login(client):    # Тест на коректное возвращение кода 200 при GET-запросе логин страницы
    response = client.get("/auth/login")
    assert response.status_code == 200

def test_login_post(client):    # Тест на коректное возвращение кода 302 (должен редирктнуть на страницу заказов)
    response = client.post("/auth/login", data={    # при POST-запросе логин страницы
        "login": "test_user",
        "password": "qwerty",
    })
    assert response.status_code == 302

def test_login_post_incorrect(client):     # Тест на коректное возвращение кода 200 (должен оставить на той же странице)
    response = client.post("/auth/login", data={    # при POST-запросе логин страницы с неправильным данными
        "login": "test_user",
        "password": "12345",
    })
    assert response.status_code == 200

