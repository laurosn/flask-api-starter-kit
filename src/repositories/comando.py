""" Defines the Comando repository """

from models.comando import Comando
from models import db


class ComandoRepository:
    """ The repository for the comando model """

    @staticmethod
    def get(id):
        """ Query a comando by id """
        return Comando.query.filter_by(id=id).one_or_none()
    
    @staticmethod
    def get_by_sistema(id):
        """ Query a comando by sistema """
        return Comando.query.filter_by(sistema_id=id).all()

    def update(self, id, name, parametros, retorno, sistema_id):
        """ Update a comando """
        comando = self.get(id)
        comando.name = name
        comando.parametros = parametros
        comando.retorno = retorno
        comando.sistema_id = sistema_id
        return comando.save()

    @staticmethod
    def create(id, name, parametros, retorno, sistema_id):
        """ Create a new comando """
        comando = Comando(id=id, name=name, parametros=parametros, retorno=retorno, sistema_id=sistema_id)

        return comando.save()

    @staticmethod
    def create_all(comandos, sistema_id):
        """ Create a new comando """
        comandos_entries = [] 
        for comando in comandos:
            new_comando = Comando(name=comando['name'], parametros=comando['parametros'], retorno=comando['retorno'], sistema_id=sistema_id)
            comandos_entries.append(new_comando)
        db.session.add_all(comandos_entries)
        db.session.commit()


    def delete(self, id):
        """ Delete a comando """
        comando = self.get(id)
        if comando:
            comando.delete()
        return comando

