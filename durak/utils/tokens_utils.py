import datetime
import jwt
from os import getenv

from utils.constants import HASH_ALG

SECRET_ACCESS_TOKEN = getenv("SECRET_ACCESS_TOKEN")
SECRET_REFRESH_TOKEN = getenv("SECRET_REFRESH_TOKEN")


def generate_access_token(login):
    return jwt.encode(
        {"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=3),
         'login': login},
        key=SECRET_ACCESS_TOKEN,
        algorithm=HASH_ALG)


def generate_refresh_token(login):
    return jwt.encode({'login': login}, key=SECRET_REFRESH_TOKEN, algorithm=HASH_ALG)


def get_info_from_refresh_token(refresh_token):
    return jwt.decode(refresh_token, SECRET_REFRESH_TOKEN, algorithms=HASH_ALG)
