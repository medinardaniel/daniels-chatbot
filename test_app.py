# test_app.py

import app
import json

def test_chat():
    app.app.testing = True
    client = app.app.test_client()

    # Send a POST request to the /chat endpoint with a JSON payload
    response = client.post('/chat', json={'message': 'Hello'})

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Parse the response JSON
    data = json.loads(response.data)

    # Assert that the response contains the 'response' key
    assert 'response' in data

    # Assert that the response is not empty
    assert data['response'] != ''