from __future__ import print_function
from dataclasses import asdict
from flask import Flask, Blueprint, make_response, jsonify, request
from os import environ
# import grpc
from requests import HTTPError, ReadTimeout, Session, Timeout
from requests.exceptions import SSLError

from app.modules.authentication.exceptions import FailedAuthorization
from app.utils.middleware.require_authentication import AuthMiddleware
from app.utils.middleware.require_authentication import require_authentication
from app.utils.load_protobuf_payload import load_to_dict
from app.modules.client.apllication.client_interface import Client


favorite_bp = Blueprint('favorite', __name__)
client = Client()


@favorite_bp.route('/product/favorite/<int:product_id>', methods=['POST'])
@require_authentication
def favorite_product(product_id):
    client_id = AuthMiddleware().authenticate()['client_id']

    request = client.favorite_product(product_id, client_id)

    return request
    