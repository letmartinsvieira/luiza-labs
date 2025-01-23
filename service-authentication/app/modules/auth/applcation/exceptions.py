from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class AuthException(Exception):
    message: str = 'auth.exception'


@abstractmethod
class AuthNotFoundException(AuthException):
    message: str = 'client.not.found'


@abstractmethod
class AuthEmailAlreadyExistException(AuthException):
    message: str = 'client.email.already.exist'