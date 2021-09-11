import os
import tempfile

import pytest
from werkzeug.security import generate_password_hash

from durak import create_app
from durak.db import get_db, init_db
from durak.utils.tokens_utils import generate_refresh_token


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({
        'TESTING': True,
        'DATABASE': db_path
    })

    with app.app_context():
        init_db()

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def user(app):
    with app.app_context():
        db = get_db()
        login = 'some_unique_user_name'
        password = 'some password'
        password_hash = generate_password_hash(password)

        db.execute('INSERT INTO users (login, password) VALUES(?, ?);',
                   (login, password_hash))
        db.commit()
        return {'login': login, 'password_hash': password_hash, 'password': password}


@pytest.fixture
def refresh_token(app, user):
    refresh_token = generate_refresh_token(user['login'])

    with app.app_context():
        db = get_db()

        db.execute('INSERT INTO tokens (login,token) VALUES(?, ?);',
                   (user['login'], refresh_token))
        db.commit()
    return refresh_token


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
