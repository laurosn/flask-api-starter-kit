"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask import request, make_response
from models.user import User, UserSchema
from models import db
from server import servidor


from util import validate_token


class UserRegisterResource(Resource):
    """ Verbs relative to the users """


    @staticmethod
    @swag_from("../swagger/user/register/POST.yml")
    def post():
        """ Create an user based on the sent information """
        post_data = request.get_json(force=True)
        print(post_data,flush=True)
        # check if user already exists
        user = User.query.filter_by(email=post_data.get('email')).first()
        if not user:
            try:
                user = User(
                    email=post_data.get('email'),
                    password=post_data.get('password')
                )
                # insert the user
                db.session.add(user)
                db.session.commit()
                # generate the auth token
                auth_token = user.encode_auth_token(user.id)
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                    'auth_token': auth_token.decode()
                }
                return make_response(jsonify(responseObject), 201)
                #return make_response(jsonify({"post": f"sistemas criados com sucesso"}), 201)
            except Exception as e:
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occurred. Please try again.',
                    'exception': e
                }
                return make_response(jsonify(responseObject), 401)
        else:
            responseObject = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return make_response(jsonify(responseObject), 202)

class UserLoginResource(Resource):
    """
    User Login Resource
    """
    @staticmethod
    @swag_from("../swagger/user/login/POST.yml")
    def post():
        # get the post data
        post_data = request.get_json(force=True)
        try:
            # fetch the user data
            user = User.query.filter_by(
                email=post_data.get('email')
            ).first()
            if user and servidor.bcrypt.check_password_hash(
                user.password, post_data.get('password')
            ):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    responseObject = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token.decode()
                    }
                    return make_response(jsonify(responseObject), 200)
            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'User does not exist.'
                }
                return make_response(jsonify(responseObject), 404)
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(responseObject), 500)
 
class UsersResource(Resource):
    """ Verbs relative to the sistemas """
    @staticmethod
    @swag_from("../swagger/user/list/GET.yml")
    @validate_token
    def get():
        """ Return all users """
        user_schema = UserSchema()
        #sistema_schema = SistemaRepository.get(id=id)
        return user_schema.dump(User.query.all(), many=True)
