from dataclasses import dataclass

from app.modules.client.applcation.exceptions import ClientNotFoundException
from app.modules.client.domain.client import Client
from app.modules.client.domain.client_factory import ClientFactory, CreateClientFactoryRequest


@dataclass
class UpdateClientUseCaseInput:
    client_id: int
    name: str
    email: str


@dataclass
class UpdateClientUseCaseOutput:
    client: Client


class UpdateClientUseCase:
    def __init__(self, client_repository):
        self.client_repository = client_repository

    def execute(self, input_data: UpdateClientUseCaseInput) -> UpdateClientUseCaseOutput:
        client = ClientFactory.create(CreateClientFactoryRequest(
            name=input_data.name,
            email=input_data.email,
            id=input_data.client_id,
        ))

        client = self.client_repository.update(client)

        if not client:
            raise ClientNotFoundException()

        return UpdateClientUseCaseOutput(client)