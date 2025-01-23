from marshmallow import fields

from app.modules.default_schema import DefaultSchema


class CreateFavoriteProductSchema(DefaultSchema):
    product_id = fields.Integer(required=True, allow_none=False)
    client_id = fields.Integer(required=True, allow_none=False)

class ListFavoriteProductSchema(DefaultSchema):
    client_id = fields.Integer(required=True, allow_none=False)
    page = fields.Integer(required=True, allow_none=True)
    limit = fields.Integer(required=True, allow_none=True)

