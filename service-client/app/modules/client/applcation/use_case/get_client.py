from dataclasses import dataclass

from app.modules.client.applcation.exceptions import ClientNotFoundException
from app.modules.client.domain.client import Client
from app.modules.client.domain.client_repository_interface import ClientRepositoryInterface


@dataclass
class GetClientUseCaseInput:
    client_id: int = None
    email: str = None


@dataclass
class GetClientUseCaseOutput:
    client: Client


class GetClientUseCase:
    def __init__(self, client_repository: ClientRepositoryInterface):
        self.client_repository = client_repository

    def execute(self, input_data: GetClientUseCaseInput) -> GetClientUseCaseOutput:
        if input_data.client_id:
            client = self.client_repository.get_by_id(input_data.client_id)

        elif input_data.email:
            client = self.client_repository.get_by_email(input_data.email)

        if not client:
            raise ClientNotFoundException()

        return GetClientUseCaseOutput(client)