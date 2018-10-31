#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import (Flask, g, session)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    @app.before_request
    def before_request():
        g.user = session.get('username', '')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .table import main as table_blueprint
    app.register_blueprint(table_blueprint, url_prefix='/table')

    from .echarts import main as echarts_blueprint
    app.register_blueprint(echarts_blueprint, url_prefix='/echarts')

    from .links import main as links_blueprint
    app.register_blueprint(links_blueprint, url_prefix='/links')

    if config.ENV != 'online':
        from .test import main as test_blueprint
        app.register_blueprint(test_blueprint, url_prefix='/test')

    return app
