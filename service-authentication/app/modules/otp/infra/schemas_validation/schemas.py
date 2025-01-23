from marshmallow import fields, validate, ValidationError

from app.modules.default_schema import DefaultSchema


class GetOTPSchema(DefaultSchema):
    id = fields.Integer(required=True, allow_none=False)

class GetOTPByCodeSchema(DefaultSchema):
    code = fields.String(required=True, allow_none=False)

class CreateOTPSchema(DefaultSchema):
    credential = fields.String(required=True, allow_none=False)

class UpdateOTPSchema(DefaultSchema):
    code = fields.String(required=True, allow_none=False)
    credential = fields.String(required=True, allow_none=False)