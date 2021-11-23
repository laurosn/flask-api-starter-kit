""" Defines the User repository """

from models.user import User
from models import db


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def get(email):
        """ Query a user by last and first name """
        return User.query.filter_by(email=email).one_or_none()

    def update(self, last_name, first_name, age):
        """ Update a user's age """
        user = self.get(last_name, first_name)
        user.age = age

        return user.save()

    @staticmethod
    def create(last_name, first_name, age):
        """ Create a new user """
        user = User(last_name=last_name, first_name=first_name, age=age)

        return user.save()

    def delete(self, last_name, first_name):
        """ Delete a user """
        user = self.get(last_name, first_name)
        if user:
            user.delete()
        return user

