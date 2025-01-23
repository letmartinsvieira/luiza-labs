from dataclasses import dataclass

from app.modules.auth.applcation.exceptions import AuthEmailAlreadyExistException
from app.modules.auth.domain.auth_repository_interface import AuthRepositoryInterface
from app.modules.auth.domain.auth_factory import AuthFactory, CreateAuthFactoryRequest


@dataclass
class CreateAuthUseCaseInput:
    type: str
    credential: str
    client_id: int


@dataclass
class CreateAuthUseCaseOutput:
    id: int


class CreateAuthUseCase:
    def __init__(self, auth_repository: AuthRepositoryInterface):
        self.auth_repository = auth_repository

    def execute(self, input_data: CreateAuthUseCaseInput):
        auth = self.auth_repository.get_by_email(input_data.credential)

        if auth:
            raise AuthEmailAlreadyExistException()

        auth = AuthFactory.create(CreateAuthFactoryRequest(
            type=input_data.type,
            credential=input_data.credential,
            client_id=input_data.client_id,
        ))

        # session = self.client_repository.begin_transaction()
        auth = self.auth_repository.create(auth)

        # self.client_repository.commit(session)

        return CreateAuthUseCaseOutput(
            id=auth.id,
        )