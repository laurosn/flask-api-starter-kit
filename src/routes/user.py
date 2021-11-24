"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import UserRegisterResource, UserLoginResource, UsersResource

USER_BLUEPRINT = Blueprint("user", __name__)
Api(USER_BLUEPRINT).add_resource(
    UserRegisterResource, "/user/register"
)

Api(USER_BLUEPRINT).add_resource(
    UserLoginResource, "/user/login"
)

Api(USER_BLUEPRINT).add_resource(
    UsersResource, "/users"
)