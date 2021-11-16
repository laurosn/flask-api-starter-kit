"""
Define the REST verbs relative to the sistemas
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import SistemaRepository
from util import parse_params


class ListaComandosBySistemaResource(Resource):
    """ Verbs relative to the sistemas """

    @staticmethod
    @swag_from("../swagger/sistema/GET_COMANDOS.yml")
    def get(id):
        """ Return an sistema key information based on his id """
        sistema = SistemaRepository.get(id=id)
        return jsonify({"sistema": sistema.comandos.json})

 