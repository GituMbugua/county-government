from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


bootstrap = Bootstrap()


def create_app(config_name):

    app = Flask(__name__)

    # creating configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    # initializing flask extensions
    bootstrap.init_app(app)

    # registering main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # registering auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')


    return app

