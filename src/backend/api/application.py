import logging

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api
from flask_jwt_extended import JWTManager

from .config import config_by_name

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] %(levelname)s: %(message)s')

db = SQLAlchemy()

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(config_by_name['dev'])

db.init_app(app)
jwt = JWTManager(app)

def create_app(config_name='dev'):
    global app
    app.config.from_object(config_by_name[config_name])

    bp = Blueprint('api', __name__, url_prefix='/api')

    api = Api(bp,
        title='WebApp',
        description='Add description here',
        version='0.0.1',
        security='Bearer Auth',
        authorizations={
            'Bearer Auth': {
                'type': 'apiKey',
                'in': 'header',
                'name': 'Authorization'
            },
        },
        ordered=True,
        terms_url='https://andrei.cioara.me',
        license='MIT',
        license_url='https://andrei.cioara.me',
    )

    from .views.dinosaur_views import api as dinosaur_ns
    api.add_namespace(dinosaur_ns)

    app.register_blueprint(bp)

    return app
