from flask import request
import jwt
from functools import wraps
from os import getenv
from utils.constants import HASH_ALG, ExpiredSignature

SECRET = getenv("SECRET")


def is_authenticated(f):
    @wraps(f)
    def decorated_function():
        print(f)
        auth = request.headers['Authorization'].split()

        if len(auth) != 2:
            return {}, 400

        auth_type, token = auth

        if auth_type != 'Bearer':
            return {}, 400  # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400

        try:
            user_info = jwt.decode(token, SECRET, HASH_ALG)
            return f(user_info=user_info)
        except jwt.ExpiredSignatureError:
            return {'error': ExpiredSignature}, 400
        except jwt.InvalidTokenError:
            return {}, 401  # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401

    return decorated_function
