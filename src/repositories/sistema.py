""" Defines the Sistema repository """

from models.sistema import Sistema
from models import db


class SistemaRepository:
    """ The repository for the sistema model """

    @staticmethod
    def get(id):
        """ Query a sistema by id """
        return Sistema.query.filter_by(id=id).one_or_none()
    
    @staticmethod
    def get_all():
        """ Query a sistema by id """
        return Sistema.query.all()


    def update(self, id, name, environment):
        """ Update a sistema """
        sistema = self.get(id)
        sistema.name = name
        sistema.environment = environment
        return sistema.save()

    @staticmethod
    def create(id, name, environment):
        """ Create a new sistema """
        sistema = Sistema(id=id, name=name, environment=environment)

        return sistema.save()

    @staticmethod
    def create_all(sistemas):
        """ Create a new sistema """
        sistemas_entries = [] 
        for sistema in sistemas:
            new_sistema = Sistema(id=int(sistema['id']), name=sistema['name'], environment=sistema['environment'])
            sistemas_entries.append(new_sistema)
        db.session.add_all(sistemas_entries)
        db.session.commit()


    def delete(self, id):
        """ Delete a sistema """
        sistema = self.get(id)
        if sistema:
            sistema.delete()
        return sistema

