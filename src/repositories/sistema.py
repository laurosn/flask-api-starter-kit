""" Defines the Sistema repository """

from models import Sistema


class SistemaRepository:
    """ The repository for the sistema model """

    @staticmethod
    def get(id):
        """ Query a sistema by id """
        return Sistema.query.filter_by(id=id).one_or_none()

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

    def delete(self, id):
        """ Delete a sistema """
        sistema = self.get(id)
        if sistema:
            sistema.delete()
        return sistema

