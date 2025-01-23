import sqlalchemy as db
from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.ext.declarative import as_declarative

# DeclarativeBase = declarative_base()


# @as_declarative()
class Base(DeclarativeBase):
    pass
    # @declared_attr
    # def __tablename__(cls):
    #     return cls.__name__.lower()