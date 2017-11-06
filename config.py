import os


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_YELLOW_URL")
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://monster:Hummingbirdcomp#@localhost/county_govt'
    Debug = True


class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://monster:Hummingbirdcomp#@localhost/county_govt_test'
    pass


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
