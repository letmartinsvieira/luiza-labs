from dataclasses import dataclass, field
import random
import time
import pyotp
import time
import jwt
import time
import os
import dotenv
import secrets
from datetime import timedelta, datetime, timezone

from app.modules.auth.domain.auth import Auth
from app.modules.auth.domain.auth_repository_interface import AuthRepositoryInterface

@dataclass
class Otp:
    code: str = None
    auth_id: int = None
    token: str = None
    id: int = None
    
    def validate_otp(self, input_code):
        return self.code == input_code
    
    def set_token(self, code: str, credential: str, client_id: int, auth_id: int):
        dotenv.load_dotenv()
        secret = os.getenv('SECRET')
        algorithm = os.getenv('ALGORITHM')
        client_id = client_id
        payload = {
            'code': str(code),
            'auth_id': int(auth_id),
            'client_id': client_id,
            'credential': credential,
            'exp': datetime.now(timezone.utc) + timedelta(seconds=320)
        }

        token = jwt.encode(payload,'secret', algorithm='HS256')
        return token
    