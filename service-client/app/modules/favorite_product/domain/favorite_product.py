from dataclasses import dataclass, field

from app.modules.favorite_product.domain.product_review import ProductReview


@dataclass
class FavoriteProduct:
    product_id: int
    client_id: int
    id: int = None

    def _validate(self):
        if not self.client_id:
            raise ValueError('Client id required')

        if not self.product_id:
            raise ValueError('Product id required')

    def __post_init__(self):
        self._validate()
