import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.modules.client.domain.client import Client
from app.modules.client.domain.client_factory import CreateClientFactoryRequest, ClientFactory
from app.modules.client.domain.client_repository_interface import ClientRepositoryInterface
from app.modules.client.infra.db.client_model import ClientModel, begin_transaction


class ClientRepository(ClientRepositoryInterface):

    def __init__(self, client_model: Client = Client):
        engine = create_engine('postgresql://postgres:postgres@svc_client_postgres:5432/service_client_db')
        Session = sessionmaker(bind=engine)
        self.session = Session()
    
    
    def create(self, client) -> Client:
        self.session.begin()

        client_model = ClientModel()

        client_model.name = client.name
        client_model.email = client.email

        self.session.add(client_model)
        self.session.commit()
        # self.session.close()

        client.id = client_model.id

        self.session.close()
        return client

    def get_by_id(self, client_id: int) -> Client | None:
        self.session.begin()
        client_model = self.session.query(ClientModel).filter(ClientModel.id == client_id).first()

        if not client_model:
            self.session.close()
            return None

        client = ClientFactory.create(
            CreateClientFactoryRequest(
                name=client_model.name,
                email=client_model.email,
            ),
        )

        self.session.close()
        return client

    def get_by_email(self, email: str) -> Client | None:
        self.session.begin()
        client_model = self.session.query(ClientModel).filter(ClientModel.email == email).first()

        if not client_model:
            self.session.close()
            return None

        client = ClientFactory.create(
            CreateClientFactoryRequest(
                name=client_model.name,
                email=client_model.email,
                id=client_model.id,
            ),
        )

        self.session.close()
        return client

    def update(self, client: Client) -> Client | None:
        self.session.begin()
        client_model = self.session.query(ClientModel).filter(ClientModel.id == client.id).first()

        if not client_model:
            self.session.close()
            return None

        client_model.name = client.name
        client_model.email = client.email

        self.session.commit()
        self.session.close()

        return client

    def delete(self, client_id: int) -> int | None:
        self.session.begin()
        client_model = self.session.query(ClientModel).filter(ClientModel.id == client_id).first()

        if not client_model:
            self.session.close()
            return

        self.session.delete(client_model)
        self.session.commit()
        self.session.close()