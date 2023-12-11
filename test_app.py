# test_app.py

import pytest
import app

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_chat(client):
    # Send a POST request to the /chat endpoint with a JSON payload
    response = client.post('/chat', json={'message': 'Hello'})

    # Assert that the response status code is 500
    assert response.status_code == 500
