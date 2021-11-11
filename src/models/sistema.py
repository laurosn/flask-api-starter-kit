"""
Define the Sistema model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Sistema(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "sistema"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    environment = db.Column(db.String(255))

    def __init__(self, id, name , environment):
        """ Create a new Sistema """
        self.id = id
        self.name = name
        self.environment = environment
