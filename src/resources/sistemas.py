"""
Define the REST verbs relative to the sistemas
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask import request

from repositories import SistemaRepository
from models import SistemaSchema, Sistema
from util import parse_params
import json

class SistemasResource(Resource):
    """ Verbs relative to the sistemas """

    @staticmethod
    @parse_params(
        Argument("sistemas", location="json", required=True, help="The id of the sistema." , )
    )
    @swag_from("../swagger/sistema/BULK_POST.yml")
    def post(sistemas):
        """ Create an sistema based on the sent information """
        json_data  = request.get_json(force=True)
        # print(json_data, flush=True)
        # print(sistemas, flush=True)
        sistemas_json = json_data['sistemas']
        #print("Sistema 0" + sistemas[0], flush=True)
        sistemas_criados = SistemaRepository.create_all(sistemas_json)
        sistema_schema = SistemaSchema()
        #sistema_schema = SistemaRepository.get(id=id)
        return sistema_schema.dump(sistemas_criados)
        #return jsonify({"sistema": sistema.json})

