from marshmallow import Schema, fields


class UserSchema(Schema):
    public_id = fields.Int()
    username = fields.Str()
    email = fields.Str()
    registered_on = fields.DateTime()
