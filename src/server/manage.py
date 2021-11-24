from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import routes

import config_params
from models import db

server = Flask(__name__)
server.debug = config_params.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config_params.DB_URI
db.init_app(server)

migrate = Migrate(server, db)
manager = Manager(server)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
