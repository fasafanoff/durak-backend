from flask import request
import jwt
from functools import wraps
from os import getenv
from utils.constants import HASH_ALG, ExpiredSignature


def required_fields(fields):
    def actual_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if request.json is None:
                return {}, 400
            for field in fields:
                if field not in request.json:
                    return {}, 400
            return function(*args, **kwargs)
        return wrapper
    return actual_decorator



#
#
# def is_authenticated(f):
#     @wraps(f)
#     def decorated_function():
#         print(f)
#         auth = request.headers['Authorization'].split()
#
#         if len(auth) != 2:
#             return {}, 400
#
#         auth_type, token = auth
#
#         if auth_type != 'Bearer':
#             return {}, 400  # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400
#
#         try:
#             user_info = jwt.decode(token, SECRET, HASH_ALG)
#             return f(user_info=user_info)
#         except jwt.ExpiredSignatureError:
#             return {'error': ExpiredSignature}, 400
#         except jwt.InvalidTokenError:
#             return {}, 401  # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401
#
#     return decorated_function
