"""
Defines the blueprint for the comando
"""
from flask import Blueprint
from flask_restful import Api

from resources import ComandoResource

COMANDO_BLUEPRINT = Blueprint("comando", __name__)
Api(COMANDO_BLUEPRINT).add_resource(
    ComandoResource, "/sistema/<int:id_sistema>/comando/<int:id>", "comando_resource"
)
