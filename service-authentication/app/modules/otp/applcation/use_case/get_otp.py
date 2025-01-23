from dataclasses import dataclass

from app.modules.otp.applcation.exceptions import OTPNotFoundException
from app.modules.otp.domain.otp import Otp
from app.modules.otp.domain.otp_repository_interface import OTPRepositoryInterface


@dataclass
class GetOTPUseCaseInput:
    id: int = None
    code : str = None


@dataclass
class GetOTPUseCaseOutput:
    otp: Otp


class GetOTPUseCase:
    def __init__(self, otp_repository: OTPRepositoryInterface):
        self.otp_repository = otp_repository

    def execute(self, input_data: GetOTPUseCaseInput) -> GetOTPUseCaseOutput:
        if input_data.id:
            otp = self.otp_repository.get_by_id(input_data.id)
        else:
            otp = self.otp_repository.get_by_code(input_data.code)

        if not otp:
            raise OTPNotFoundException()

        return GetOTPUseCaseOutput(otp)