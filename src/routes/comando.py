"""
Defines the blueprint for the comando
"""
from flask import Blueprint
from flask_restful import Api

from resources import ComandoResource, ComandoExecutionResource

COMANDO_BLUEPRINT = Blueprint("comando", __name__)
Api(COMANDO_BLUEPRINT).add_resource(
    ComandoExecutionResource, "/sistema/<int:sistema_id>/comando/<int:id>/execute"
)

Api(COMANDO_BLUEPRINT).add_resource(
    ComandoResource, "/sistema/<int:sistema_id>/comando/<int:id>"
)
