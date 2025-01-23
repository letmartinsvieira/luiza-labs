from dataclasses import dataclass

from app.modules.auth.domain.auth import Auth


@dataclass
class CreateAuthFactoryRequest:
    type: str
    credential: str
    client_id: int
    id: int = None

class AuthFactory:

    @staticmethod
    def create(request: CreateAuthFactoryRequest) -> Auth:
        auth = Auth(
            type=request.type,
            credential=request.credential,
            client_id=request.client_id,
            id=request.id,
        )

        return auth