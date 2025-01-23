from abc import abstractmethod
from dataclasses import dataclass

@abstractmethod
class FailedAuthorization(Exception):
    message: str = 'authorization.failed.exception'