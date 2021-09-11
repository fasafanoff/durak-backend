import time
import jwt
from flask import (
    Blueprint, request
)
from werkzeug.security import check_password_hash, generate_password_hash

from durak.db import get_db
from durak.routes.middlewares import required_fields
from durak.utils.tokens_utils import generate_access_token, generate_refresh_token, get_info_from_refresh_token
from durak.utils.validators import is_password_valid, is_login_valid
from utils.constants import SIGN_IN_ERROR, HASH_ALG, ExpiredSignature, SIGN_UP_ERROR

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['POST'])
@required_fields(['login', 'password'])
def login_route():
    form = request.json
    login, password = form['login'], form['password']

    db = get_db()

    user = db.execute("SELECT password FROM users WHERE login=?",
                      (login,)).fetchone()

    if user is None:
        return {'error': SIGN_IN_ERROR}, 400

    user_password = user['password']

    if user_password is None or not \
            check_password_hash(user_password, password):
        return {'error': SIGN_IN_ERROR}, 400

    access_token = generate_access_token(login)
    refresh_token = generate_refresh_token(login)

    db.execute("INSERT INTO tokens VALUES(?,?)", (refresh_token, login))
    db.commit()
    return {
        'refresh_token': refresh_token,
        'access_token': access_token
    }


@bp.route('/token', methods=['POST'])
@required_fields(['refresh-token'])
def token_route():
    body = request.json

    refresh_token = body['refresh-token']
    if refresh_token is None:
        return {}, 403
    try:
        db = get_db()
        is_refresh_token_in_db = db.execute("SELECT token FROM tokens WHERE token=?",
                                            (refresh_token,)).fetchone() is not None

        if not is_refresh_token_in_db:
            return {}, 403

        user_info = get_info_from_refresh_token(refresh_token)
        access_token = generate_access_token(user_info['login'])
        return {'access-token': access_token}, 200
    except jwt.ExpiredSignatureError:
        return {'error': ExpiredSignature}, 400
    except jwt.InvalidTokenError:
        return {}, 401


@bp.route('/signup', methods=['POST'])
@required_fields(['login', 'password'])
def signup_route():
    form = request.json
    login = form['login'].strip()

    if not is_login_valid(login):
        return {'error': SIGN_UP_ERROR}, 400

    password = form['password'].strip()
    if is_password_valid(password):
        return {'error': SIGN_UP_ERROR}, 400

    hashedpassword = generate_password_hash(password)
    time_stamp_now = time.time()
    db = get_db()

    db.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)",
               (login, hashedpassword, None, time_stamp_now, None))
    db.commit()

    return {}
