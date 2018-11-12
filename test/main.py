from flask import Flask, jsonify, request, make_response, abort


def hello(*args):
    response = {'name': 'Hello World', 'args': args}
    return make_response(jsonify(response), 200)


if __name__ == '__main__':
    print("Initiating Flask REST Service...")
    app = Flask(__name__)
    @app.route('/')
    def index():
        id = request.args.get('id', '000001')
        data = hello(id)
        # print(data)
        return data

    app.run(debug=True)