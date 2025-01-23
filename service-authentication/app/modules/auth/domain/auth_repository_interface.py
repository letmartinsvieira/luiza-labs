from abc import ABC, abstractclassmethod, abstractmethod
from dataclasses import dataclass


from app.modules.auth.domain.auth import Auth


class AuthRepositoryInterface(ABC):
    
    # @abstractmethod
    # def rollback(self) -> None:
    #     raise NotImplementedError
    #
    # @abstractmethod
    # def commit(self) -> None:
    #     raise NotImplementedError
    
    @abstractmethod
    def create(self, auth: Auth) -> Auth:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, id: int) -> Auth | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_client_id(self, client_id: int) -> Auth | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_email(self, email: str) -> Auth | None:
        raise NotImplementedError

    # @abstractmethod
    # def update(self, auth: Auth) -> Auth | None:
    #     raise NotImplementedError

    # @abstractmethod
    # def delete(self, auth_id: int) -> int | None:
    #     raise NotImplementedError

    def get_by_email(self, email: str) -> Auth | None:
        raise NotImplementedError