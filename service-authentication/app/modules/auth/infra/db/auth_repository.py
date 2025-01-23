import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.modules.auth.domain.auth import Auth
from app.modules.auth.domain.auth_factory import CreateAuthFactoryRequest, AuthFactory
from app.modules.auth.domain.auth_repository_interface import AuthRepositoryInterface
from app.modules.auth.infra.db.auth_model import AuthModel, begin_auth_transaction


class AuthRepository(AuthRepositoryInterface):

    def __init__(self, auth_model: Auth = Auth):
        engine = create_engine('postgresql://postgres:postgres@svc_authentication_postgres:5432/service_authentication_db')
        Session = sessionmaker(bind=engine)
        self.session = Session()
    
    # def rollback(self):
    #     return self.session.rollback()
    #
    # def commit(self):
    #     return self.session.commit()

    def create(self, auth) -> Auth:
        self.session.begin()

        auth_model = AuthModel()

        auth_model.type = auth.type
        auth_model.credential = auth.credential
        auth_model.client_id = auth.client_id

        self.session.add(auth_model)
        self.session.commit()
        # self.session.close()

        auth.id = auth_model.id
        return auth
    
    def get_by_client_id(self, client_id: int) -> Auth | None:
        self.session.begin()
        auth_model = self.session.query(AuthModel).filter(AuthModel.client_id == client_id).first()

        if not auth_model:
            self.session.close()
            return None

        self.session.close()
        return auth_model

    def get_by_id(self, id: int) -> Auth | None:
        self.session.begin()
        auth_model = self.session.query(AuthModel).filter(AuthModel.id == id).first()

        if not auth_model:
            self.session.close()
            return None

        self.session.close()
        return auth_model

    def get_by_email(self, email: str) -> Auth | None:
        self.session.begin()
        auth_model = self.session.query(AuthModel).filter(AuthModel.credential == email).first()

        if not auth_model:
            self.session.close()
            return None

        auth = AuthFactory.create(
            CreateAuthFactoryRequest(
                type=auth_model.type,
                credential=auth_model.credential,
                client_id=auth_model.client_id,
                id=auth_model.id,
            ),
        )

        self.session.close()
        return auth

    # def update(self, client: Client) -> Client | None:
    #     self.session.begin()
    #     client_model = self.session.query(ClientModel).filter(ClientModel.id == client.id).first()

    #     if not client_model:
    #         self.session.close()
    #         return None

    #     client_model.name = client.name
    #     client_model.email = client.email

    #     self.session.commit()
    #     self.session.close()

    #     return client

    # def delete(self, client_id: int) -> int | None:
    #     self.session.begin()
    #     client_model = self.session.query(ClientModel).filter(ClientModel.id == client_id).first()

    #     if not client_model:
    #         self.session.close()
    #         return

    #     self.session.delete(client_model)
    #     self.session.commit()
    #     self.session.close()