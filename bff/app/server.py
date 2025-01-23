import json
from http.client import HTTPException

from flask import Flask, jsonify, request
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from os import environ
from app.modules.authentication import auth_api as auth_server
from app.modules.client import client_api as client_server
from app.modules.product import product_api as product_server
from app.modules.favorites import favorites_api as favorite_server


api_port = int(environ['API_PORT'])

server = Flask(__name__)
# server.config['JWT_TOKEN_LOCATION'] = ['bearer']
server.register_blueprint(client_server.client_bp)
server.register_blueprint(auth_server.auth_pb)
server.register_blueprint(product_server.product_bp)
server.register_blueprint(favorite_server.favorite_bp)

@server.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

server.run(host='0.0.0.0', port=api_port)
