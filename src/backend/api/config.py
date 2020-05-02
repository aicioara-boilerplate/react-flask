import os

basedir = os.path.abspath(os.path.dirname(__file__))



class Config:
    SECRET_KEY = "Changeme"
    JWT_SECRET_KEY = "Changeme2"
    JWT_BLACKLIST_ENABLED = False
    JWT_BLACKLIST_TOKEN_CHECKS = ['refresh']

    SQLALCHEMY_DATABASE_URI = '{PROTOCOL}://{USER}:{PASSWORD}@{HOST}/{DATABASE}{PARAMS}'.format(
        PROTOCOL="postgres",
        USER="user",
        PASSWORD="password",
        HOST="localhost:5432",
        DATABASE="my_database",
        PARAMS="",
    )
    # Delete this to use postgres
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.sqlite3')

    DEBUG = False
    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/signals/
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevelopmentConfig(Config):
    DEBUG = True



class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database_test.sqlite3')
    PRESERVE_CONTEXT_ON_EXCEPTION = False



class ProductionConfig(Config):
    DEBUG = False



config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
