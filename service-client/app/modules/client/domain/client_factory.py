from dataclasses import dataclass

from app.modules.client.domain.client import Client


@dataclass
class CreateClientFactoryRequest:
    name: str
    email: str
    id: int = None

class ClientFactory:

    @staticmethod
    def create(request: CreateClientFactoryRequest) -> Client:
        client = Client(
            name=request.name,
            email=request.email,
            id=request.id,
        )

        return client