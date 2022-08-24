from flask import Flask
from .user_router import user
from .whitelist_router import whitelist


def init_app(app: Flask):
    app.register_blueprint(user, url_prefix='/api')
    app.register_blueprint(whitelist, url_prefix='/api')
