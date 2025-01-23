from dataclasses import dataclass


@dataclass
class ProductException(Exception):
    message: str = "product.exception"


@dataclass
class ProductNotFoundException(ProductException):
    message: str = "product.not.found"