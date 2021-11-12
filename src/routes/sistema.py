"""
Defines the blueprint for the sistema
"""
from flask import Blueprint
from flask_restful import Api

from resources import SistemaResource

SISTEMA_BLUEPRINT = Blueprint("sistema", __name__)
Api(SISTEMA_BLUEPRINT).add_resource(
    SistemaResource, "/sistema/<int:id>", "/sistema"
)
