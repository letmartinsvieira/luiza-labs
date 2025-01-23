import sqlalchemy as db
import datetime
# import sleep
from sqlalchemy.ext.indexable import index_property
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.modules.client.infra.db.client_model import ClientModel

# from app.database.orm_config.declarative_base import Base


Base = declarative_base()
class FavoriteProductModel(Base):
    __tablename__  = 'favorite_product'

    id = db.Column(db.Integer,  primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey(ClientModel.id, ondelete='CASCADE'))
    product_id = db.Column(db.Integer)
    
    unq_client_id_product_id = db.UniqueConstraint(client_id, product_id, name='unq_client_id_product_id')


def begin_transaction():
    db = create_engine('postgresql://postgres:postgres@svc_client_postgres:5432/service_client_db')

    Session = sessionmaker(bind=db)
    session = Session()

    Base.metadata.create_all(bind=db)

    session.close()
    return db