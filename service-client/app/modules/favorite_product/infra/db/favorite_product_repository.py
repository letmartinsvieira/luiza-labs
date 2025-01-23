from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import redis

from app.modules.favorite_product.domain.favorite_product import FavoriteProduct
from app.modules.favorite_product.domain.favorite_product_repository_interface import FavoriteProductRepositoryInterface
from app.modules.favorite_product.infra.db.favorite_product_model import FavoriteProductModel


class FavoriteProductRepository(FavoriteProductRepositoryInterface):
    def __init__(self):
        engine = create_engine('postgresql://postgres:postgres@svc_client_postgres:5432/service_client_db')
        self.r = redis.Redis(host='product_redis', port=6379, db=0, decode_responses=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_favorite_product(self, favorite_product: FavoriteProduct) -> FavoriteProduct:
        self.session.begin()

        favorite_product_model = FavoriteProductModel()

        favorite_product_model.product_id = favorite_product.product_id
        favorite_product_model.client_id = favorite_product.client_id

        self.session.add(favorite_product_model)
        self.session.commit()

        favorite_product.id = favorite_product_model.id

        self.r.set(favorite_product.client_id, favorite_product.product_id)

        self.session.close()
        return favorite_product

    def list_favorite_products(self, client_id: int, page: int = 1, limit: int = 10) -> list[FavoriteProduct]:
        self.session.begin()
        favorite_product_model = self.session.query(FavoriteProductModel) \
            .filter(FavoriteProductModel.client_id == client_id).first()
        
        if not favorite_product_model:
            self.session.close()
            return None
        
        # favorite_product =  FavoriteProduct(
        #     id=favorite_product_model.id,
        #     product_id=favorite_product_model.product_id,
        #     client_id=favorite_product_model.client_id,
        # )

        self.session.close()
        return favorite_product_model

    def get_favorite_product(self, client_id: int, product_id: int) -> FavoriteProduct | None:
        self.session.begin()
        favorite_product_model = self.session.query(FavoriteProductModel) \
            .filter(FavoriteProductModel.product_id == product_id) \
            .filter(FavoriteProductModel.client_id == client_id) \
            .first()

        if not favorite_product_model:
            self.session.close()
            return None

        favorite_product = FavoriteProduct(
            id=favorite_product_model.id,
            product_id=favorite_product_model.product_id,
            client_id=favorite_product_model.client_id,
        )

        self.session.close()
        return favorite_product
    