from dataclasses import dataclass

from app.modules.favorite_product.domain.favorite_product import FavoriteProduct


@dataclass
class ListFavoriteProductUseCaseInput:
    client_id: int
    page: int = 1
    limit: int = 5

@dataclass
class ListFavoriteProductUseCaseOutput:
    products: list[FavoriteProduct]


class ListFavoriteProductUseCase:
    def __init__(self, favorite_product_repository):
        self.favorite_product_repository = favorite_product_repository

    def execute(self, input_data: ListFavoriteProductUseCaseInput):
        products = self.favorite_product_repository.list(
            input_data.page,
            input_data.limit
        )

        return ListFavoriteProductUseCaseOutput(products)