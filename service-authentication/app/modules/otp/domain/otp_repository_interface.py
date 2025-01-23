from abc import ABC, abstractclassmethod, abstractmethod
from dataclasses import dataclass


from app.modules.otp.domain.otp import Otp


class OTPRepositoryInterface(ABC):
    
    # @abstractmethod
    # def rollback(self) -> None:
    #     raise NotImplementedError
    #
    # @abstractmethod
    # def commit(self) -> None:
    #     raise NotImplementedError
    
    @abstractmethod
    def create(self, otp: Otp) -> Otp:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, auth_id: int) -> Otp | None:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_code(self, code: str) -> Otp | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, otp: Otp) -> Otp | None:
        raise NotImplementedError

    # @abstractmethod
    # def delete(self, auth_id: int) -> int | None:
    #     raise NotImplementedError
