from flask.testing import FlaskClient
from app import app
import pytest


@pytest.fixture
def client() -> FlaskClient:
    return app.test_client()


def test_get_all_users(client: FlaskClient) -> None:
    actual = client.get('/users')
    assert actual.status_code == 200
