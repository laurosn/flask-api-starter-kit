from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


from .user import User, UserSchema
from .sistema import Sistema, SistemaSchema
from .comando import Comando, ComandoSchema
from .blacklist_token import BlacklistToken, BlacklistTokenSchema