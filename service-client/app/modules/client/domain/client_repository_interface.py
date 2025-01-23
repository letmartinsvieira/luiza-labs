from abc import ABC, abstractclassmethod, abstractmethod
from dataclasses import dataclass


from app.modules.client.domain.client import Client


class ClientRepositoryInterface(ABC):
    
    # @abstractmethod
    # def rollback(self) -> None:
    #     raise NotImplementedError
    #
    # @abstractmethod
    # def commit(self) -> None:
    #     raise NotImplementedError
    
    @abstractmethod
    def create(self, client: Client) -> Client:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, client_id: int) -> Client | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_email(self, email: str) -> Client | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, client: Client) -> Client | None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, client_id: int) -> int | None:
        raise NotImplementedError
