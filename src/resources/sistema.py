"""
Define the REST verbs relative to the sistemas
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import SistemaRepository
from models.sistema import SistemaSchema
from util import parse_params, validate_token


class SistemaResource(Resource):
    """ Verbs relative to the sistemas """

    @staticmethod
    @swag_from("../swagger/sistema/GET.yml")
    @validate_token
    def get(id):
        """ Return an sistema key information based on his id """
        sistema_schema = SistemaSchema()
        #sistema_schema = SistemaRepository.get(id=id)
        return sistema_schema.dump(SistemaRepository.get(id=id))
        #return jsonify({"sistema": sistema.json})

    @staticmethod
    @parse_params(
        Argument("name", location="json", required=True, help="The id of the sistema."),
        Argument("environment", location="json", required=True, help="The id of the sistema.")
    )
    @swag_from("../swagger/sistema/POST.yml")
    @validate_token
    def post(id, name, environment):
        """ Create an sistema based on the sent information """
        sistema = SistemaRepository.create(
            id=id, name=name, environment=environment
        )
        sistema_schema = SistemaSchema()
        #sistema_schema = SistemaRepository.get(id=id)
        return sistema_schema.dump(sistema)
        #return jsonify({"sistema": sistema.json})

    @staticmethod
    @parse_params(
        Argument("name", location="json", required=True, help="The id of the sistema."),
        Argument("environment", location="json", required=True, help="The id of the sistema.")
    )
    @swag_from("../swagger/sistema/PUT.yml")
    @validate_token
    def put(id, name, environment):
        """ Update an sistema based on the sent information """
        repository = SistemaRepository()
        sistema = repository.update(id=id, name=name, environment=environment)
        sistema_schema = SistemaSchema()
        #sistema_schema = SistemaRepository.get(id=id)
        return sistema_schema.dump(sistema).data
        #return jsonify({"sistema": sistema.json})


    @staticmethod
    @swag_from("../swagger/sistema/DELETE.yml")
    @validate_token
    def delete(id):
        repository = SistemaRepository()
        sistema = repository.delete(id=id)
        if sistema:
            return jsonify({"delete": f"sistema {id} excluido com sucesso"})
        else:
            return jsonify({"delete": f"sistema {id} nao encontrado"})
 