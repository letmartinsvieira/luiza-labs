from dataclasses import dataclass

from app.modules.auth.applcation.exceptions import AuthNotFoundException
from app.modules.auth.domain.auth import Auth
from app.modules.auth.domain.auth_factory import AuthFactory, CreateAuthFactoryRequest


@dataclass
class UpdateAuthUseCaseInput:
    id: int
    credential: str


@dataclass
class UpdateAuthUseCaseOutput:
    auth: Auth


class UpdateAuthUseCase:
    def __init__(self, auth_repository):
        self.auth_repository = auth_repository

    def execute(self, input_data: UpdateAuthUseCaseInput) -> UpdateAuthUseCaseOutput:
        auth = AuthFactory.create(CreateAuthFactoryRequest(
            credential=input_data.credential,
        ))

        auth = self.auth_repository.update(auth)

        if not auth:
            raise AuthNotFoundException()

        return UpdateAuthUseCaseOutput(auth)