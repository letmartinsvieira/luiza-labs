from dataclasses import dataclass
import random
import time
import pyotp
import time
import jwt
import time
import os
import dotenv
import json
from datetime import timedelta, datetime, timezone

from app.modules.otp.applcation.exceptions import OTPEmailAlreadyExistException
from app.modules.otp.domain.otp_repository_interface import OTPRepositoryInterface
from app.modules.otp.domain.otp_factory import OTPFactory, CreateOTPFactoryRequest
from app.modules.auth.domain.auth_repository_interface import AuthRepositoryInterface


@dataclass
class CreateOTPUseCaseInput:
    credential : str = None


@dataclass
class CreateOTPUseCaseOutput:
    code: str


class CreateOTPUseCase:
    def __init__(
        self,
        otp_repository: OTPRepositoryInterface,
        auth_repository: AuthRepositoryInterface,
        
    ):
        self.otp_repository = otp_repository
        self.auth_repository = auth_repository

    def execute(self, input_data: CreateOTPUseCaseInput):
    
        auth = self.auth_repository.get_by_email(input_data.credential)
        credential_auth_id = auth.id
        otp = self.otp_repository.get_by_id(credential_auth_id)

        if otp:
            raise OTPEmailAlreadyExistException(otp)

        secret_key = pyotp.random_base32()
        otp_uri = pyotp.totp.TOTP('JBSWY3DPEHPK3PXP').provisioning_uri(name='alice@google.com', issuer_name='Secure App')
        otp = pyotp.parse_uri(otp_uri)
    
        otp = OTPFactory.create(CreateOTPFactoryRequest(
            auth_id=credential_auth_id,
            code=otp.now(),
        ))

        otp = self.otp_repository.create(otp)

        return CreateOTPUseCaseOutput(
            code=otp.code,
        )
    