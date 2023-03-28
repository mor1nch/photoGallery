from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from dao.model.user import User

from setup_db import db


class Photo(db.Model):
    __tablename__ = 'photo'
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    url = Column(String(), nullable=False)
    owner_id = Column(Integer(), ForeignKey(User.id), nullable=False)
    owner = relationship("User")


class PhotoSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    url = fields.Str()
    owner_id = fields.Int()
