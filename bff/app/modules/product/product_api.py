from __future__ import print_function
from dataclasses import asdict
from flask import Flask, Blueprint, make_response, jsonify, request
from os import environ
import requests
import json
from requests import HTTPError, ReadTimeout, Session, Timeout
from requests.exceptions import SSLError

from app.modules.authentication.exceptions import FailedAuthorization
from app.utils.middleware.require_authentication import require_authentication
from app.utils.load_protobuf_payload import load_to_dict



product_bp = Blueprint('product', __name__)

@product_bp.route('/product', methods=['GET'])
def get_products():
    page = request.args.get('page', 1)
    limit = request.args.get('limit', 5)
    url = 'http://test_service_product:5023/products?page={}&limit={}'.format(page, limit)
    response = requests.get(url)
    return response.json()

@product_bp.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    url = 'http://test_service_product:5023/product/{}'.format(id)
    response = requests.get(url)
    return response.json()  
   

