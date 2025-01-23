from abc import ABC, abstractmethod

from app.modules.favorite_product.domain.favorite_product import FavoriteProduct


class FavoriteProductRepositoryInterface(ABC):

    @abstractmethod
    def create_favorite_product(self, favorite_product: FavoriteProduct) -> FavoriteProduct:
        raise NotImplementedError

    @abstractmethod
    def list_favorite_products(self, client_id: int, page: int = 1, limit: int = 10) -> list[FavoriteProduct]:
        raise NotImplementedError

    @abstractmethod
    def get_favorite_product(self, client_id: int, product_id: int) -> FavoriteProduct | None:
        raise NotImplementedError