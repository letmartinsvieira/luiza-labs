from abc import ABC, abstractmethod

from app.modules.product.domain.product import Product


class ProductRepositoryInterface(ABC):

    @abstractmethod
    def list(self, page: int = 1, limit: int = 5) -> list:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, product_id: int) -> Product | None:
        raise NotImplementedError