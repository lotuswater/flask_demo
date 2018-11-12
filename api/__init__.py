from __future__ import print_function

import click
from flask.cli import FlaskGroup, run_command
from flask import Flask, current_app
from flask_restful import Api

from api.routes import register_routes


def init_app(app):
    api = Api(app)
    # add routes
    register_routes(api)
    api.init_app(app)


def create_app():
    app = current_app or Flask(__name__)
    init_app(app)
    return app


def create(group):
    app = create_app()
    group.app = app

    return app


@click.group(cls=FlaskGroup, create_app=create)
def manager():
    """Management script for API"""


manager.add_command(run_command, "runserver")
