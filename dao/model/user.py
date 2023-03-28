from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer

from setup_db import db


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), nullable=False)
    surname = Column(String(), nullable=False)
    phone = Column(String(), nullable=False)
    password = Column(String(), nullable=False)


class UserSchema(Schema):
    id = fields.Int()
    first_name = fields.Str()
    surname = fields.Str()
    phone = fields.Str()
    password = fields.Str()
