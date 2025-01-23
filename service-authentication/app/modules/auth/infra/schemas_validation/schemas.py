from marshmallow import fields, validate, ValidationError

from app.modules.default_schema import DefaultSchema


class GetAuthSchema(DefaultSchema):
    client_id = fields.Integer(required=True, allow_none=False)

class GetAuthByEmailSchema(DefaultSchema):
    email = fields.String(required=True, allow_none=False)

class CreateAuthSchema(DefaultSchema):
    type = fields.String(required=True, allow_none=False)
    credential = fields.String(required=True, allow_none=False)
    client_id = fields.Integer(required=True)