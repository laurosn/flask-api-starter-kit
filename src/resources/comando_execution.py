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
from util import validate_token
from models import ComandoSchema


class ComandoExecutionResource(Resource):
    """ Verbs relative to the comandos """

    @staticmethod
    @swag_from("../swagger/execution/GET.yml")
    @validate_token
    def get(id, sistema_id):
        """ Return an comando key information based on his id """
        sistema_repository = SistemaRepository() 
        sistema = sistema_repository.get(id=sistema_id)
        if not sistema:
            return make_response(jsonify({"post": f"sistema {sistema_id} nao encontrado"}), 404)
        comando = ComandoRepository.get(id=id)
        print(comando, flush=True)
        if not comando:
            return make_response(jsonify({"post": f"comando {id} nao encontrado"}), 404)
        # comando_schema = ComandoSchema()
        #sistema_schema = SistemaRepository.get(id=id)
        return make_response(jsonify({"retorno": comando.retorno}), 404)

 