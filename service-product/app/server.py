import json
from http.client import HTTPException

from flask import Flask
from os import environ
from app.modules.product.infra import server as product_server

api_port = int(environ['API_PORT'])

server = Flask(__name__)
server.register_blueprint(product_server.product_bp)

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

# def _register_blueprints() {}