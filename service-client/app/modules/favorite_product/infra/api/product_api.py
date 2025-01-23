from os import environ

from requests import HTTPError, ReadTimeout, Session, Timeout
from requests.exceptions import SSLError

from app.modules.favorite_product.application.exceptions import ProductNotFoundException
from app.modules.favorite_product.domain.product_api_interface import ProductApiInterface, ProductReview, Product


class ProductApi(ProductApiInterface):
    def __init__(self) -> None:
        self.request = Session()
        self.base_url = environ['BASE_URL']
        self.request_timeout = 30
        self.headers = {'Content-Type': 'application/json'}

    def _get_headers(self, custom_headers):
        return {**self.headers, **custom_headers}

    def _get(self, url, params={}, custom_headers={}, *args, **kwargs):
        url = f'{self.base_url}{url}'
        return self.request.get(
            url,
            params=params,
            headers=self._get_headers(custom_headers),
            timeout=self.request_timeout,
            *args, **kwargs,
        )

    def list_products(self, page: int, limit: int) -> list[Product]:
        pass

    def get_product_by_id(self, product_id: int) -> Product | None:
        try:
            response = self._get(f'/product/{product_id}')

            response.raise_for_status()
            response_data = response.json()

            return Product(**response_data['data']['product'])
        except HTTPError as e:
            status_code = e.response.status_code
            response_error = e.response.json()

            if status_code == 500:
                raise Exception(response_error)

            if status_code == 404:
                raise ProductNotFoundException()

    def list_product_reviews(self, product_id: int, page: int, limit: int) -> list[ProductReview]:
        pass