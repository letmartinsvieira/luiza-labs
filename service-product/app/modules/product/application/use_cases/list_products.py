from dataclasses import dataclass

from app.modules.product.domain.product import Product


@dataclass
class ListProductsUseCaseInput:
    page: int = 1
    limit: int = 5

@dataclass
class ListProductsUseCaseOutput:
    products: list[Product]


class ListProductsUseCase:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def execute(self, input_data: ListProductsUseCaseInput):
        products = self.product_repository.list(input_data.page, input_data.limit)

        return ListProductsUseCaseOutput(products)