import json

from durak import create_app
from durak.db import get_db

from durak.utils.tokens_utils import generate_access_token, generate_refresh_token


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_login_no_data(client):
    response = client.post('/auth/login')
    assert response.status_code == 400


def test_login_empty_data(client):
    response = client.post('/auth/login', json={})
    assert response.status_code == 400


def test_login_wrong_data(client):
    response = client.post('/auth/login',
                           json={'login': 'wrong login', 'password': 'password'})
    assert response.status_code == 400


def test_login_wrong_password(client, user):
    response = client.post('/auth/login',
                           json={
                               'login': user['login'],
                               'password': 'wrong password'
                           })
    assert response.status_code == 400


def test_login_correct_data(client, user, app):
    response = client.post('/auth/login', json=user)
    assert response.status_code == 200
    login = user['login']

    access_token = generate_access_token(login)
    refresh_token = generate_refresh_token(login)

    assert response.data is not None

    response_data = json.loads(response.data)

    assert response_data['access_token'] == access_token
    assert response_data['refresh_token'] == refresh_token
    with app.app_context():
        db = get_db()
        assert db.execute("SELECT * FROM tokens WHERE login=? and token=?",
                          (login, refresh_token)).fetchone() is not None
