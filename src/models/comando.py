"""
Define the Comando model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Comando(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Comando model """

    __tablename__ = "comando"
    __table_args__ = {
        'extend_existing': True,
    }

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    parametros = db.Column(db.String(255))
    sistema_id = db.Column(db.Integer, db.ForeignKey('sistema.id'))

    def __init__(self, id, name , parametros, sistema_id):
        """ Create a new Sistema """
        self.id = id
        self.name = name
        self.parametros = parametros
        self.sistema_id = sistema_id
