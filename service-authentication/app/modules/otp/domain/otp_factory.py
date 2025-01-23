from dataclasses import dataclass

from app.modules.otp.domain.otp import Otp


@dataclass
class CreateOTPFactoryRequest:
    code: str = None
    auth_id: int = None
    token: str = None
    id: int = None

class OTPFactory:

    @staticmethod
    def create(request: CreateOTPFactoryRequest) -> Otp:
        otp = Otp(
            code=request.code,
            token=request.token,
            auth_id=request.auth_id,
            id=request.id,
        )

        return otp