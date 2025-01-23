from dataclasses import dataclass


@dataclass
class FavoriteProductException(Exception):
    message: str = 'favorite.product.exception'


@dataclass
class FavoriteProductNotFoundException(FavoriteProductException):
    message: str = 'favorite.product.not.found'


@dataclass
class ProductNotFoundException(FavoriteProductException):
    message: str = 'product.not.found'


@dataclass
class FavoriteProductAlreadyExistException(FavoriteProductException):
    message: str = 'favorite.product.already.exist'