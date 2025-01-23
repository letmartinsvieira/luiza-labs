from marshmallow import fields, validate, ValidationError

from app.modules.default_schema import DefaultSchema


class GetClientSchema(DefaultSchema):
    client_id = fields.Integer(required=True, allow_none=False)


class GetClientByEmailSchema(DefaultSchema):
    email = fields.String(required=True, allow_none=False)


class CreateClientSchema(DefaultSchema):
    name = fields.String(required=True, allow_none=False)
    email = fields.String(required=True, allow_none=False)


class UpdateClientSchema(DefaultSchema):
    client_id = fields.Integer(required=True, allow_none=False)
    name = fields.String(required=True, allow_none=False)
    email = fields.String(required=True, allow_none=False)


class DeleteClientSchema(DefaultSchema):
    client_id = fields.Integer(required=True, allow_none=False)