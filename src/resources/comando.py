"""
Define the REST verbs relative to the comandos
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import ComandoRepository,SistemaRepository
from util import parse_params
from models import ComandoSchema


class ComandoResource(Resource):
    """ Verbs relative to the comandos """

    @staticmethod
    @swag_from("../swagger/comando/GET.yml")
    def get(id, sistema_id):
        """ Return an comando key information based on his id """
        sistema_repository = SistemaRepository() 
        sistema = sistema_repository.get(id=sistema_id)
        if not sistema:
            return jsonify({"post": f"sistema {sistema_id} nao encontrado"})
        comando = ComandoRepository.get(id=id)
        comando_schema = ComandoSchema()
        #sistema_schema = SistemaRepository.get(id=id)
        return comando_schema.dump(comando)

    @staticmethod
    @parse_params(
        Argument("parametros", location="json", required=True, help="The name of the comando."),
        Argument("name", location="json", required=True, help="The name of the sistema.")
    )
    @swag_from("../swagger/comando/POST.yml")
    def post(id, name, parametros, sistema_id):
        """ Create an comando based on the sent information """
        sistema_repository = SistemaRepository() 
        sistema = sistema_repository.get(id=sistema_id)
        if not sistema:
            return jsonify({"post": f"sistema {sistema_id} nao encontrado"})
        comando = ComandoRepository.create(
            id=id, name=name, parametros=parametros, sistema_id=sistema_id
        )
        comando_schema = ComandoSchema()
        #sistema_schema = SistemaRepository.get(id=id)
        return comando_schema.dump(comando)

    @staticmethod
    @parse_params(
        Argument("parametros", location="json", required=True, help="The name of the comando."),
        Argument("name", location="json", required=True, help="The name of the sistema.")
    )
    @swag_from("../swagger/comando/PUT.yml")
    def put(id, name, parametros, sistema_id):
        """ Update an comando based on the sent information """
        sistema_repository = SistemaRepository() 
        sistema = sistema_repository.get(id=sistema_id)
        if not sistema:
            return jsonify({"put": f"sistema {sistema_id} nao encontrado"})

        repository = ComandoRepository()
        comando = repository.update(id=id, name=name, parametros=parametros, sistema_id=sistema_id)
        comando_schema = ComandoSchema()
        #sistema_schema = SistemaRepository.get(id=id)
        return comando_schema.dump(comando)


    @staticmethod
    @swag_from("../swagger/comando/DELETE.yml")
    def delete(id, sistema_id):
        sistema_repository = SistemaRepository() 
        sistema = sistema_repository.get(id=sistema_id)
        if not sistema:
            return jsonify({"delete": f"sistema {sistema_id} nao encontrado"})

        repository = ComandoRepository()
        comando = repository.delete(id=id)
        if comando:
            return jsonify({"delete": f"comando {id} excluido com sucesso"})
        else:
            return jsonify({"delete": f"comando {id} nao encontrado"})
 