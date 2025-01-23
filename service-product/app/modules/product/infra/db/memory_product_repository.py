from app.modules.product.domain.product import Product
from app.modules.product.domain.product_repository_interface import ProductRepositoryInterface


class MemoryProductRepository(ProductRepositoryInterface):
    def __init__(self):
        self.products = [
            Product(
                id=1,
                title="Product 1",
                price=100.0,
                brand="Brand 1",
                image="https://www.example.com/product1.jpg",
                review_score=0,
            ),
            Product(
                id=2,
                title="Product 2",
                price=200.0,
                brand="Brand 2",
                image="https://www.example.com/product2.jpg",
            ),
            Product(
                id=3,
                title="Product 3",
                price=300.0,
                brand="Brand 3",
                image="https://www.example.com/product3.jpg",
                review_score=5,
            ),
            Product(
                id=4,
                title="Product 4",
                price=400.0,
                brand="Brand 4",
                image="https://www.example.com/product4.jpg",
                review_score=1,
            ),
            Product(
                id=5,
                title="Product 5",
                price=500.0,
                brand="Brand 5",
                image="https://www.example.com/product5.jpg",
                review_score=7,
            ),
            Product(
                id=6,
                title="Product 6",
                price=600.0,
                brand="Brand 6",
                image="https://www.example.com/product6.jpg",
                review_score=3,
            ),
            Product(
                id=7,
                title="Product 7",
                price=700.0,
                brand="Brand 7",
                image="https://www.example.com/product7.jpg",
                review_score=4,
            ),
            Product(
                id=8,
                title="Product 8",
                price=800.0,
                brand="Brand 8",
                image="https://www.example.com/product8.jpg",
                review_score=6,
            ),
            Product(
                id=9,
                title="Product 9",
                price=900.0,
                brand="Brand 9",
                image="https://www.example.com/product9.jpg",
                review_score=1,
            ),
            Product(
                id=10,
                title="Product 10",
                price=1000.0,
                brand="Brand 10",
                image="https://www.example.com/product10.jpg",
                review_score=8,
            ),
            Product(
                id=11,
                title="Product 11",
                price=1100.0,
                brand="Brand 11",
                image="https://www.example.com/product11.jpg",
                review_score=9,
            ),
            Product(
                id=12,
                title="Product 12",
                price=1200.0,
                brand="Brand 12",
                image="https://www.example.com/product12.jpg",
                review_score=4,
            ),
            Product(
                id=13,
                title="Product 13",
                price=1300.0,
                brand="Brand 13",
                image="https://www.example.com/product13.jpg",
                review_score=5,
            ),
            Product(
                id=14,
                title="Product 14",
                price=1400.0,
                brand="Brand 14",
                image="https://www.example.com/product14.jpg",
                review_score=6,
            ),
            Product(
                id=15,
                title="Product 15",
                price=1500.0,
                brand="Brand 15",
                image="https://www.example.com/product15.jpg",
                review_score=7,
            ),
        ]

    def get_by_id(self, product_id: int) -> Product | None:
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def list(self, page: int = 1, limit: int = 5) -> list:
        return self.products[
            (page - 1) * limit : page * limit
        ]