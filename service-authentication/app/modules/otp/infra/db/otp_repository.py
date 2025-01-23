import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.modules.otp.domain.otp import Otp
from app.modules.otp.domain.otp_factory import CreateOTPFactoryRequest, OTPFactory
from app.modules.otp.domain.otp_repository_interface import OTPRepositoryInterface
from app.modules.otp.infra.db.otp_model import OTPModel, begin_transaction


class OTPRepository(OTPRepositoryInterface):

    def __init__(self, otp_model: Otp = Otp):
        engine = create_engine('postgresql://postgres:postgres@svc_authentication_postgres:5432/service_authentication_db')
        Session = sessionmaker(bind=engine)
        self.session = Session()
    
    # def rollback(self):
    #     return self.session.rollback()
    #
    # def commit(self):
    #     return self.session.commit()

    def create(self, otp) -> Otp:
        self.session.begin()

        otp_model = OTPModel()

        otp_model.auth_id = otp.auth_id
        otp_model.code = otp.code
        otp_model.token = otp.token

        self.session.add(otp_model)
        self.session.commit()
        # self.session.close()

        otp.id = otp_model.id
        return otp

    def get_by_id(self, id: int) -> Otp | None:
        self.session.begin()
        otp_model = OTPModel()
        otp_model = self.session.query(OTPModel).filter(OTPModel.id == id).first()

        if not otp_model:
            self.session.close()
            return None

        self.session.close()
        return otp_model
    
    def get_by_code(self, code: str) -> Otp | None:
        self.session.begin()
        otp_model = OTPModel()
        otp_model = self.session.query(OTPModel).filter(OTPModel.code == code).first()

        if not otp_model:
            self.session.close()
            return None

        self.session.close()
        return otp_model


    def update(self, otp: Otp) -> Otp | None:
        self.session.begin()

        otp_model = self.session.query(OTPModel).filter(OTPModel.id == otp.id).first()

        if not otp_model:
            self.session.close()
            return None
        
        otp_model.code=otp.code,
        otp_model.token=otp.token,
        
        self.session.commit()
        self.session.close()

        return otp
