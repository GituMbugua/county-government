import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):

    pass


class DevConfig(Config):

    Debug = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}