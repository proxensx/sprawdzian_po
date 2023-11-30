from flask.testing import FlaskClient
from app import app
from app import users
import pytest


@pytest.fixture
def client() -> FlaskClient:
    return app.test_client()


def test_create_user(client):
    initial_count = len(users)
    data = {'name': 'Wojciech', 'lastname': 'Oczkowski'}
    response = client.post('/users', json=data)
    assert response.status_code == 201
    assert len(users) == initial_count + 1