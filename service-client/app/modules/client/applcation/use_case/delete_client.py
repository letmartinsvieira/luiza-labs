from dataclasses import dataclass

from app.modules.client.applcation.exceptions import ClientNotFoundException


@dataclass
class DeleteClientUseCaseInput:
    client_id: int


class DeleteClientUseCase:
    def __init__(self, client_repository):
        self.client_repository = client_repository

    def execute(self, input_data: DeleteClientUseCaseInput):
        client_id = self.client_repository.delete(input_data.client_id)

        if not client_id:
            raise ClientNotFoundException()

        return