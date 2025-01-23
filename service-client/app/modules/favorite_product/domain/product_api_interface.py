from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Product:
    id: int
    title: str
    price: float
    image: str
    brand: str
    review_score: float


@dataclass
class ProductReview:
    id: int
    score: int
    comment: str


class ProductApiInterface(ABC):

    @abstractmethod
    def list_products(self, page: int, limit: int) -> list[Product]:
        raise NotImplementedError

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Product | None:
        raise NotImplementedError

    @abstractmethod
    def list_product_reviews(self, product_id: int, page: int, limit: int) -> list[ProductReview]:
        raise NotImplementedError