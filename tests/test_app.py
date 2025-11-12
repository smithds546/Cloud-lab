# tests/test_app.py
import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World! Welcome to COC105 CI/CD Lab!"}
