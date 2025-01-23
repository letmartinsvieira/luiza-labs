from dataclasses import dataclass

from app.modules.auth.applcation.exceptions import AuthNotFoundException
from app.modules.auth.domain.auth import Auth
from app.modules.auth.domain.auth_repository_interface import AuthRepositoryInterface


@dataclass
class GetAuthUseCaseInput:
    client_id: int = None
    credential: str = None


@dataclass
class GetAuthUseCaseOutput:
    auth: Auth


class GetAuthUseCase:
    def __init__(self, auth_repository: AuthRepositoryInterface):
        self.auth_repository = auth_repository

    def execute(self, input_data: GetAuthUseCaseInput) -> GetAuthUseCaseOutput:
        if input_data.client_id:
            auth = self.auth_repository.get_by_client_id(input_data.client_id)
        else:
            auth = self.auth_repository.get_by_email(input_data.credential)

        if not auth:
            raise AuthNotFoundException()

        return GetAuthUseCaseOutput(auth)