from marshmallow import EXCLUDE, Schema


class DefaultSchema(Schema):
    class Meta:
        unknown = EXCLUDE