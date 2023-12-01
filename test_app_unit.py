from flask.testing import FlaskClient
from app import app
import pytest


@pytest.fixture
def client() -> FlaskClient:
    return app.test_client()


def test_get_all_users(client: FlaskClient) -> None:
    actual = client.get('/users')
    assert actual.status_code == 200


def test_get_user(client: FlaskClient) -> None:
    actual = client.get(f'/users/1')
    assert actual.status_code == 200


def test_create_user(client: FlaskClient) -> None:
    new_data = {"name": "Wojciech", "lastname": "Oczkowski"}
    actual = client.post('/users', json=new_data)
    assert actual.status_code == 201
    

def test_update_user(client: FlaskClient) -> None:
    pass
    

def test_replace_user(client: FlaskClient) -> None:
    pass


def test_delete_user(client: FlaskClient) -> None:
    actual = client.delete(f"/users/4")
    assert actual.status_code == 400