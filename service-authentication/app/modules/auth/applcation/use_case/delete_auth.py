from dataclasses import dataclass

from app.modules.auth.applcation.exceptions import AuthNotFoundException


@dataclass
class DeleteAuthUseCaseInput:
    id: int


class DeleteAuthUseCase:
    def __init__(self, auth_repository):
        self.auth_repository = auth_repository

    def execute(self, input_data: DeleteAuthUseCaseInput):
        id = self.auth_repository.delete(input_data.id)

        if not id:
            raise AuthNotFoundException()

        return