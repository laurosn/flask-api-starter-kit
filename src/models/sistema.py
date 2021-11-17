"""
Define the Sistema model
"""
from . import db, ma
from .abc import BaseModel, MetaBaseModel
from .comando import ComandoSchema
# from dataclasses import dataclass
#from .. import ma
# from marshmallow_sqlalchemy import ModelSchema



class Sistema(db.Model):
    """ The User model """

    __tablename__ = "sistema"
    __table_args__ = {
        'extend_existing': True,
    }

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    environment = db.Column(db.String(255))
    #comandos = db.relationship(Comando)
    comandos = db.relationship('Comando', backref='sistema',
                                 lazy='dynamic')

    def __init__(self, id, name , environment, comandos = []):
        """ Create a new Sistema """
        self.id = id
        self.name = name
        self.environment = environment
        self.comandos = comandos
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class SistemaSchema(ma.SQLAlchemyAutoSchema):

    comandos = ma.Nested(ComandoSchema, default=[], many=True)
    class Meta:
        model = Sistema
        load_instance = True
        sqla_session = db.session