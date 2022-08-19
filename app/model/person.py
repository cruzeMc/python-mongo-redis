from marshmallow import Schema, fields


class PersonSchema(Schema):
    _id = fields.Int()
    age = fields.Int()
    name = fields.Str()
    city = fields.Str()

