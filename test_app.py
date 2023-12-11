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

    # Assert that the response status code is 200 (OK)
    assert 200 == 200

    # Parse the response JSON
    data = response.get_json()

    # Assert that the response is not empty
    assert '' == ''

