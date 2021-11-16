from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .sistema import Sistema
from .comando import Comando