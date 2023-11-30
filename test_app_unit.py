from app import get_all_users
from app import app

def test_get_all_users() -> None:
    actual = get_all_users()
    assert actual.status_code == 200