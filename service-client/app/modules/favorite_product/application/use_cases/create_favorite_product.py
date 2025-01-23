from dataclasses import dataclass

from app.modules.favorite_product.application.exceptions import ProductNotFoundException, \
    FavoriteProductAlreadyExistException
from app.modules.favorite_product.domain.favorite_product import FavoriteProduct
from app.modules.favorite_product.domain.favorite_product_repository_interface import FavoriteProductRepositoryInterface
from app.modules.favorite_product.domain.product_api_interface import ProductApiInterface


@dataclass
class CreateFavoriteProductUseCaseInput:
    product_id: int
    client_id: int


@dataclass
class CreateFavoriteProductUseCaseOutput:
    product_id: int
    client_id: int
    favorite_product_id: int


class CreateFavoriteProductUseCase:
    def __init__(
        self,
        favorite_product_repository: FavoriteProductRepositoryInterface,
        product_api: ProductApiInterface,
    ):
        self.product_api = product_api
        self.favorite_product_repository = favorite_product_repository

    def execute(self, input_data: CreateFavoriteProductUseCaseInput) -> CreateFavoriteProductUseCaseOutput:
        self.product_api.get_product_by_id(input_data.product_id)

        favorite_product = self.favorite_product_repository \
            .get_favorite_product(
                input_data.client_id,
                input_data.product_id,
            )

        if favorite_product:
            raise FavoriteProductAlreadyExistException()

        favorite_product = FavoriteProduct(
            product_id=input_data.product_id,
            client_id=input_data.client_id,
        )

        favorite_product = self.favorite_product_repository.create_favorite_product(favorite_product)

        return CreateFavoriteProductUseCaseOutput(
            product_id=input_data.product_id,
            client_id=input_data.client_id,
            favorite_product_id=favorite_product.id,
        )