"""
Define the Comando model
"""
from . import db, ma
from .abc import BaseModel, MetaBaseModel
# from server import ma

class Comando(db.Model):
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

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class ComandoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comando
        sqla_session = db.session