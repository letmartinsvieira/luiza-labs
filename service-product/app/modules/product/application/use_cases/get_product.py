from dataclasses import dataclass

from app.modules.product.application.exceptions import ProductNotFoundException
from app.modules.product.domain.product import Product
from app.modules.product.domain.product_repository_interface import ProductRepositoryInterface


@dataclass
class GetProductUseCaseInput:
    product_id: int


@dataclass
class GetProductUseCaseOutput:
    product: Product


class GetProductUseCase:

    def __init__(self, product_repository: ProductRepositoryInterface):
        self.repository = product_repository

    def execute(self, input_data: GetProductUseCaseInput) -> GetProductUseCaseOutput:
        product = self.repository.get_by_id(input_data.product_id)

        if not product:
            raise ProductNotFoundException

        return GetProductUseCaseOutput(product)