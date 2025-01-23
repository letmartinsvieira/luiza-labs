from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class ClientException(Exception):
    message: str = 'client.exception'


@abstractmethod
class ClientNotFoundException(ClientException):
    message: str = 'client.not.found'


@abstractmethod
class ClientEmailAlreadyExistException(ClientException):
    message: str = 'client.email.already.exist'