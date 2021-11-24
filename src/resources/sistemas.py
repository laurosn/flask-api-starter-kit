"""
Define the REST verbs relative to the sistemas
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask import request, make_response

from repositories import SistemaRepository
from models.sistema import SistemaSchema, Sistema
from util import parse_params, validate_token
import json

class SistemasResource(Resource):
    """ Verbs relative to the sistemas """

    @staticmethod
    @swag_from("../swagger/sistemas/GET.yml")
    @validate_token
    def get():
        """ Return all sistemas """
        sistema_schema =SistemaSchema()
        #sistema_schema = SistemaRepository.get(id=id)
        return sistema_schema.dump(SistemaRepository.get_all(), many=True)
        #sistema = SistemaRepository.get(id=id)
        #return jsonify({"sistema": sistema.comandos.json})


    @staticmethod
    @parse_params(
        Argument("sistemas", location="json", required=True, help="The id of the sistema." , )
    )
    @swag_from("../swagger/sistemas/POST.yml")
    @validate_token
    def post(sistemas):
        """ Create an sistema based on the sent information """
        json_data  = request.get_json(force=True)
        sistemas_json = json_data['sistemas']
        SistemaRepository.create_all(sistemas_json)
        return make_response(jsonify({"post": f"sistemas criados com sucesso"}), 200)

        #return jsonify({"sistema": sistema.json})

