"""
Define the REST verbs relative to the comandos
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import ComandoRepository,SistemaRepository
from util import parse_params


class ComandoResource(Resource):
    """ Verbs relative to the comandos """

    @staticmethod
    @swag_from("../swagger/comando/GET.yml")
    def get(id, id_sistema):
        """ Return an comando key information based on his id """
        sistema_repository = SistemaRepository() 
        sistema = sistema_repository.get(id=id_sistema)
        if not sistema:
            return jsonify({"post": f"sistema {id_sistema} nao encontrado"})
        comando = ComandoRepository.get(id=id)
        return jsonify({"comando": comando.json})

    @staticmethod
    @parse_params(
        Argument("parametros", location="json", required=True, help="The name of the comando."),
        Argument("name", location="json", required=True, help="The name of the sistema.")
    )
    @swag_from("../swagger/comando/POST.yml")
    def post(id, name, parametros, id_sistema):
        """ Create an comando based on the sent information """
        sistema_repository = SistemaRepository() 
        sistema = sistema_repository.get(id=id_sistema)
        if not sistema:
            return jsonify({"post": f"sistema {id_sistema} nao encontrado"})
        comando = ComandoRepository.create(
            id=id, name=name, parametros=parametros, id_sistema=id_sistema
        )
        return jsonify({"comando": comando.json})

    @staticmethod
    @parse_params(
        Argument("parametros", location="json", required=True, help="The name of the comando."),
        Argument("name", location="json", required=True, help="The name of the sistema.")
    )
    @swag_from("../swagger/comando/PUT.yml")
    def put(id, name, parametros, id_sistema):
        """ Update an comando based on the sent information """
        sistema_repository = SistemaRepository() 
        sistema = sistema_repository.get(id=id_sistema)
        if not sistema:
            return jsonify({"put": f"sistema {id_sistema} nao encontrado"})

        repository = ComandoRepository()
        comando = repository.update(id=id, name=name, parametros=parametros, id_sistema=id_sistema)
        return jsonify({"comando": comando.json})


    @staticmethod
    @swag_from("../swagger/comando/DELETE.yml")
    def delete(id, id_sistema):
        sistema_repository = SistemaRepository() 
        sistema = sistema_repository.get(id=id_sistema)
        if not sistema:
            return jsonify({"delete": f"sistema {id_sistema} nao encontrado"})

        repository = ComandoRepository()
        comando = repository.delete(id=id)
        if comando:
            return jsonify({"delete": f"comando {id} excluido com sucesso"})
        else:
            return jsonify({"delete": f"comando {id} nao encontrado"})
 