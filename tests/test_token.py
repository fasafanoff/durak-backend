import json
from durak.utils.tokens_utils import generate_access_token


def test_token_no_data(client):
    no_data_response = client.post('/auth/token')
    assert no_data_response.status_code == 400


def test_token_no_token(client):
    no_token_response = client.post('/auth/token', json={})
    assert no_token_response.status_code == 400


def test_token_correct_data(client, app, user, refresh_token):
    response = client.post('/auth/token',
                           json={'refresh-token': refresh_token})

    assert response.status_code == 200

    assert response.data is not None

    correct_access_token = generate_access_token(user['login'])
    correct_token_response_data = json.loads(response.data)

    access_token = correct_token_response_data['access-token']

    assert access_token == correct_access_token
