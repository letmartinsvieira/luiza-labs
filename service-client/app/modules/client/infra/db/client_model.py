import sqlalchemy as db
import datetime
# import sleep
from sqlalchemy.ext.indexable import index_property
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
# from app.database.orm_config.declarative_base import Base


Base = declarative_base()
class ClientModel(Base):
    __tablename__  = 'client'

    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, index=True, nullable=False)
    created_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    index_email = db.Index('idx_email', email)

    # favorite_product = relationship('favorite_product', cascade="all,delete", backref="parent")

def begin_transaction():
    db = create_engine('postgresql://postgres:postgres@svc_client_postgres:5432/service_client_db')

    Session = sessionmaker(bind=db)
    session = Session()
    
    Base.metadata.create_all(bind=db)

    session.close()
    return db