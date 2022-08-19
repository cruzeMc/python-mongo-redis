from datetime import datetime

from ..model.user import *


def get_user2(username):
    user_schema = UserSchema()
    user_schema.public_id = 1
    user_schema.username = username
    user_schema.email = 'cruze.m.mcfarlane@gmail.com'
    user_schema.registered_on = datetime.datetime.utcnow()
    return user_schema
