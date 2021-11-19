"""
Define the REST verbs relative to the comandos
"""

from flasgger import swag_from
from flask.json import jsonify
from flask import make_response
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy import exc

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
            return make_response(jsonify({"post": f"sistema {sistema_id} nao encontrado"}), 404)
        comando = ComandoRepository.get(id=id)
        if not comando:
            return make_response(jsonify({"post": f"comando {id} nao encontrado"}), 404)
        comando_schema = ComandoSchema()
        #sistema_schema = SistemaRepository.get(id=id)
        return comando_schema.dump(comando)

    @staticmethod
    @parse_params(
        Argument("parametros", location="json", required=True, help="The name of the comando."),
        Argument("name", location="json", required=True, help="The name of the sistema.")
    )
    @swag_from("../swagger/comando/POST.yml")
    def post(id, name, parametros, retorno, sistema_id):
        """ Create an comando based on the sent information """
        sistema_repository = SistemaRepository() 
        sistema = sistema_repository.get(id=sistema_id)
        if not sistema:
            return make_response(jsonify({"post": f"sistema {sistema_id} nao encontrado"}), 404)
        try:
            comando = ComandoRepository.create(
            id=id, name=name, parametros=parametros, retorno=retorno, sistema_id=sistema_id
            )
        except exc.IntegrityError:
            return make_response(jsonify({"post": f"comando {id} ja existe"}), 409)
        comando_schema = ComandoSchema()
        #sistema_schema = SistemaRepository.get(id=id)
        return comando_schema.dump(comando)

    @staticmethod
    @parse_params(
        Argument("parametros", location="json", required=True, help="The name of the comando."),
        Argument("name", location="json", required=True, help="The name of the sistema.")
    )
    @swag_from("../swagger/comando/PUT.yml")
    def put(id, name, parametros, retorno, sistema_id):
        """ Update an comando based on the sent information """
        sistema_repository = SistemaRepository() 
        sistema = sistema_repository.get(id=sistema_id)
        if not sistema:
            return jsonify({"put": f"sistema {sistema_id} nao encontrado"})

        repository = ComandoRepository()
        comando = repository.update(id=id, name=name, parametros=parametros, retorno=retorno, sistema_id=sistema_id)
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
 