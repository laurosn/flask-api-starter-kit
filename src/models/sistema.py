"""
Define the Sistema model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Sistema(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "sistema"
    __table_args__ = {
        'extend_existing': True,
    }

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    environment = db.Column(db.String(255))
    comandos = db.relationship('Comando', backref='sistema',
                                lazy='dynamic')

    def __init__(self, id, name , environment, comandos = tuple()):
        """ Create a new Sistema """
        self.id = id
        self.name = name
        self.environment = environment
        self.comandos = comandos
