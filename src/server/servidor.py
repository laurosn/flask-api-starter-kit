from flasgger import Swagger
from flask import Flask
from flask.blueprints import Blueprint

import server.config_params
import routes
from models import db, ma
from flask_bcrypt import Bcrypt


# config your API specs
# you can define multiple specs in the case your api has multiple versions
# ommit configs to get the default (all views exposed in /spec url)
# rule_filter is a callable that receives "Rule" object and
#   returns a boolean to filter in only desired views

app = Flask(__name__)
app.config["SWAGGER"] = {
    "swagger_version": "2.0",
    "title": "Application",
    "specs": [
        {
            "version": "0.0.1",
            "title": "Application",
            "endpoint": "spec",
            "route": "/application/spec",
            "rule_filter": lambda rule: True,  # all in
        }
    ],
    "static_url_path": "/apidocs",
}

Swagger(app)

app.debug = server.config_params.DEBUG
app.config["SQLALCHEMY_DATABASE_URI"] = server.config_params.DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = server.config_params.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)
db.app = app
ma.init_app(app)
ma.app = app
bcrypt = Bcrypt(app)
for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint, url_prefix=server.config_params.APPLICATION_ROOT)

if __name__ == "__main__":
    app.run(host=server.config_params.HOST, port=server.config_params.PORT)
