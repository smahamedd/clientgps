from marshmallow import Schema, fields, validate


class ClientSchema(Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(required=True)
    app_version = fields.String(required=True)
    added_datetime = fields.DateTime(dump_only=True)


class ClientUpdateSchema(Schema):
    app_version = fields.String(validate=validate.Length(min=1))


class ClientDeleteSchema(Schema):
    id = fields.Integer(required=True)
