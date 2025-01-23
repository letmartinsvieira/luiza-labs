from dataclasses import dataclass
import pyotp
from pyotp import TOTP

from app.modules.otp.applcation.exceptions import OTPNotFoundException
from app.modules.auth.applcation.exceptions import AuthNotFoundException
from app.modules.auth.domain.auth import Auth
from app.modules.otp.domain.otp import Otp
from app.modules.auth.domain.auth_repository_interface import AuthRepositoryInterface
from app.modules.otp.domain.otp_repository_interface import OTPRepositoryInterface
from app.modules.otp.domain.otp_factory import OTPFactory, CreateOTPFactoryRequest


@dataclass
class UpdateOTPUseCaseInput:
    code: str = None
    credential: str = None

@dataclass
class UpdateOTPUseCaseOutput:
    otp: Otp 


class UpdateOTPUseCase:
    def __init__(
        self,
        otp_repository: OTPRepositoryInterface,
        auth_repository: AuthRepositoryInterface,
    ):
        self.otp_repository = otp_repository
        self.auth_repository = auth_repository

    def execute(self, input_data: UpdateOTPUseCaseInput) -> UpdateOTPUseCaseOutput:
        otp = self.otp_repository.get_by_code(input_data.code)
        auth = self.auth_repository.get_by_id(otp.auth_id)
        
        user_token = Otp(otp).set_token(otp.code, auth.credential, auth.client_id, otp.auth_id)

        response = OTPFactory.create(
            CreateOTPFactoryRequest(
                id=otp.id,
                auth_id=auth.id,
                code=otp.code,
                token=user_token,
            )
        )        

        otp = self.otp_repository.update(response)
        
        if not auth:
            raise AuthNotFoundException
        if not otp:
            raise OTPNotFoundException()

        return UpdateOTPUseCaseOutput(otp)
    