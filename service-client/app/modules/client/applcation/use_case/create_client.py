from dataclasses import dataclass

from app.modules.client.applcation.exceptions import ClientEmailAlreadyExistException
from app.modules.client.domain.client_repository_interface import ClientRepositoryInterface
from app.modules.client.domain.client_factory import ClientFactory, CreateClientFactoryRequest


@dataclass
class CreateClientUseCaseInput:
    name: str
    email: str


@dataclass
class CreateClientUseCaseOutput:
    client_id: int


class CreateClientUseCase:
    def __init__(self, client_repository: ClientRepositoryInterface):
        self.client_repository = client_repository

    def execute(self, input_data: CreateClientUseCaseInput):
        client = self.client_repository.get_by_email(input_data.email)

        if client:
            raise ClientEmailAlreadyExistException()

        client = ClientFactory.create(CreateClientFactoryRequest(
            name=input_data.name,
            email=input_data.email,
        ))

        # session = self.client_repository.begin_transaction()
        client = self.client_repository.create(client)

        # self.client_repository.commit(session)

        return CreateClientUseCaseOutput(
            client_id=client.id,
        )