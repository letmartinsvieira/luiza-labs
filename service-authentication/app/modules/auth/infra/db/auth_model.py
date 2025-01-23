import sqlalchemy as db
import datetime
# import sleep
from sqlalchemy.ext.indexable import index_property
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# from app.database.orm_config.declarative_base import Base


Base = declarative_base()
class AuthModel(Base):
    __tablename__  = 'auth'

    id = db.Column(db.Integer,  primary_key=True)
    type = db.Column(db.String, nullable=False)
    credential = db.Column(db.String, index=True, nullable=False)
    client_id = db.Column(db.Integer)
    is_active = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)


# class OTPAuthModel(Base):
#     __tablename__ = 'otp_auth'

#     id = db.Column(db.Integer,  primary_key=True)
#     auth_id = db.Column(db.Integer)
#     code = db.Column(db.Integer)
#     code_has_been_used = db.Column(db.Boolean)
#     token = db.Column(db.String)
#     created_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)
#     updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)


def begin_auth_transaction():
    # sleep(1000)
    db = create_engine('postgresql://postgres:postgres@svc_authentication_postgres:5432/service_authentication_db')
    # db = create_engine('sqlite:///service_client_db')
    Session = sessionmaker(bind=db)
    session = Session()
    
    Base.metadata.create_all(bind=db)

    session.close()
    return db