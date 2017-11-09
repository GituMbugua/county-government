from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options

from flask_login import LoginManager


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = 'auth.login'


def create_app(config_name):

    app = Flask(__name__)

    # creating configurations
    app.config.from_object(config_options[config_name])
    # config_options[config_name].init_app(app)

    # initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # registering main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # registering auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')
   
    # # registering api blueprint
    # from .api import api as api_blueprint
    # app.register_blueprint(api_blueprint)
    return app
