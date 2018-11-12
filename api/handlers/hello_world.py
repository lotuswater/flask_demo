from __future__ import print_function

from flask import jsonify, request, make_response, abort
from api.handlers.base import BaseResource


class HelloWorld(BaseResource):
    def get(self):
        response = {'name': 'Hello World', 'args': request.args}
        return make_response(jsonify(response), 200)