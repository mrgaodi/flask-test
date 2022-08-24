from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.settings import ProdConfig, DevConfig

db = SQLAlchemy()


def create_app(env="dev"):

    app = Flask(__name__)

    db.init_app(app)

    app.config.from_object(ProdConfig if env == 'prod' else DevConfig)

    from app import router
    router.init_app(app)
    return app
