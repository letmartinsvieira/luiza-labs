import sqlalchemy as db
import datetime
# import sleep
import json
from sqlalchemy.ext import mutable
from sqlalchemy.ext.indexable import index_property
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.modules.otp.infra.db.json_encode import JsonEncodedDict

from app.modules.auth.infra.db.auth_model import AuthModel


Base = declarative_base()


class OTPModel(Base):
    __tablename__ = 'otp_auth'

    id = db.Column(db.Integer,  primary_key=True)
    auth_id = db.Column(db.Integer, db.ForeignKey(AuthModel.id))
    code = db.Column(db.String)
    token = db.Column(db.String)
    created_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)



def begin_transaction():
    db = create_engine('postgresql://postgres:postgres@svc_authentication_postgres:5432/service_authentication_db')

    Session = sessionmaker(bind=db)
    session = Session()
    
    Base.metadata.create_all(bind=db)

    session.close()
    return db