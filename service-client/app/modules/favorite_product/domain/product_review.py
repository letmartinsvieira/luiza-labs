from dataclasses import dataclass


@dataclass
class ProductReview:
    product_id: int
    score: int
    comment: str
    id: int = None

    def _validate(self):
        if not self.product_id:
            raise ValueError('Product id required')

        if not self.score:
            raise ValueError('Score required')

        if not self.comment:
            raise ValueError('Comment required')

    def __post_init__(self):
        self._validate()