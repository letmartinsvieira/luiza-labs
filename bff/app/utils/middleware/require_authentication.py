
import os
import jwt
import dotenv
import secrets
from functools import wraps
from datetime import timedelta, datetime, timezone

from flask import request

from app.modules.authentication.exceptions import FailedAuthorization

class AuthMiddleware:

    @staticmethod
    def is_valid_token(token):

        try:
            decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
            return decoded
        except Exception as e:
            print(str(e))

    def authenticate(self):
        auth_token = request.headers["Authorization"].split(" ")[1]
        decode = self.is_valid_token(auth_token)

        if not auth_token or not decode:
            raise FailedAuthorization('Unauthorized', 401)
    
        return decode


def require_authentication(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        AuthMiddleware().authenticate()
        return f(*args, **kwargs)

    return wrap
