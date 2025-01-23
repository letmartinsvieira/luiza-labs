from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class OTPException(Exception):
    message: str = 'otp.exception'


@abstractmethod
class OTPNotFoundException(OTPException):
    message: str = 'otp.not.found'


@abstractmethod
class OTPEmailAlreadyExistException(OTPException):
    message: str = 'otp.email.already.exist'