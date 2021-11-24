"""
Define the REST verbs relative to the sistemas
"""

from flasgger import swag_from
from flask.json import jsonify
from flask import request, make_response

from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import ComandoRepository, SistemaRepository
from util import parse_params, validate_token
from models.comando import ComandoSchema 
from sqlalchemy import exc


class ComandosResource(Resource):
    """ Verbs relative to the sistemas """

    @staticmethod
    @swag_from("../swagger/comandos/GET.yml")
    @validate_token
    def get(id):
        """ Return an sistema key information based on his id """
        comando_schema =ComandoSchema()
        #sistema_schema = SistemaRepository.get(id=id)
        return comando_schema.dump(ComandoRepository.get_by_sistema(id=id), many=True)
        #sistema = SistemaRepository.get(id=id)
        #return jsonify({"sistema": sistema.comandos.json})

    @staticmethod
    @parse_params(
        Argument("comandos", location="json", required=True, help="The list of comandos." , )
    )
    @swag_from("../swagger/comandos/POST.yml")
    @validate_token
    def post(id, comandos):
        """ Create an sistema based on the sent information """
        #print(comandos, flush=True)
        sistema_repository = SistemaRepository() 
        sistema = sistema_repository.get(id=id)
        if not sistema:
            return make_response(jsonify({"post": f"sistema {id} nao encontrado"}), 404)

        json_data  = request.get_json(force=True)
        comandos_json = json_data['comandos']
        try:
            ComandoRepository.create_all(comandos_json, id)
        except exc.IntegrityError:
            return make_response(jsonify({"post": f"Comando duplicado"}), 409)

        return make_response(jsonify({"post": f"comandos para o sistema {id} criados com sucesso"}), 200)


