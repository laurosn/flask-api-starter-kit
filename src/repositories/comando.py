""" Defines the Comando repository """

from models import Comando


class ComandoRepository:
    """ The repository for the comando model """

    @staticmethod
    def get(id):
        """ Query a comando by id """
        return Comando.query.filter_by(id=id).one_or_none()

    def update(self, id, name, parametros, sistema_id):
        """ Update a comando """
        comando = self.get(id)
        comando.name = name
        comando.parametros = parametros
        comando.sistema_id = sistema_id
        return comando.save()

    @staticmethod
    def create(id, name, parametros, sistema_id):
        """ Create a new comando """
        comando = Comando(id=id, name=name, parametros=parametros, sistema_id=sistema_id)

        return comando.save()

    def delete(self, id):
        """ Delete a comando """
        comando = self.get(id)
        if comando:
            comando.delete()
        return comando

