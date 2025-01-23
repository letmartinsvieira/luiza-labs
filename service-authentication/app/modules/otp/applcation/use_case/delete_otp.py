from dataclasses import dataclass

from app.modules.otp.applcation.exceptions import OTPNotFoundException


@dataclass
class DeleteOTPUseCaseInput:
    id: int


class DeleteOTPUseCase:
    def __init__(self, otp_repository):
        self.otp_repository = otp_repository

    def execute(self, input_data: DeleteOTPUseCaseInput):
        id = self.otp_repository.delete(input_data.id)

        if not id:
            raise OTPNotFoundException()

        return