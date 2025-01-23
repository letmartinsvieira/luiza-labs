from dataclasses import dataclass, field


@dataclass
class Auth:
    type: str
    credential: str
    client_id: int
    id: int = None

    def _validate(self):
        if not self.type:
            raise ValueError('Auth type required')

        if not self.credential:
            raise ValueError('Auth credential required')
        
        if not self.client_id:
            raise ValueError('Auth client_id required')

    def __post_init__(self):
        self._validate()
