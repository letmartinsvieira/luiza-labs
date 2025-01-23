from dataclasses import dataclass


@dataclass
class Product:
    id: int
    title: str
    price: float
    brand: str
    image: str
    review_score: int = 0

    def _validate(self):
        if self.price <= 0:
            raise ValueError("Price must be greater than zero")

        if self.title is None or self.title == "":
            raise ValueError("Title cannot be empty")

    def __post_init__(self):
        self._validate()