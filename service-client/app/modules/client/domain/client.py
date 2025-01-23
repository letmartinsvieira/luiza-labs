from dataclasses import dataclass, field


@dataclass
class Client:
    name: str
    email: str
    id: int = None

    def _validate(self):
        if not self.name:
            raise ValueError('Client name required')

        if not self.email:
            raise ValueError('Client email required')

    def __post_init__(self):
        self._validate()
