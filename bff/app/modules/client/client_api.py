from __future__ import print_function
from dataclasses import asdict
from flask import Flask, Blueprint, make_response, jsonify, request
from os import environ
# import grpc
from requests import HTTPError, ReadTimeout, Session, Timeout
from requests.exceptions import SSLError

from app.utils.middleware.require_authentication import AuthMiddleware
from app.modules.authentication.exceptions import FailedAuthorization
from app.utils.middleware.require_authentication import require_authentication
from app.utils.load_protobuf_payload import load_to_dict
from app.modules.client.apllication.client_interface import Client
from app.modules.authentication.application.auth_interface import AuthInterface


client_bp = Blueprint('client', __name__)
client = Client()

@client_bp.route('/client/update', methods=['PUT'])
@require_authentication
def update_client():
    data = request.json

    try:
        client_id = AuthMiddleware().authenticate()['client_id']
        
        response = client.update_client(data, data) 
        
        return data
    
    except Exception as e:    
        return make_response(jsonify(
            message='error',
            data=str('e'),
        ), 400)


@client_bp.route('/client/<int:id>', methods=['GET'])
@require_authentication
def get_client_by_id(id):
    try:
        response = client.get_by_client_id(id)
        return make_response(jsonify(
            message='client',
            data=response,
        ))
    except FailedAuthorization as e:
        return make_response(jsonify(
                message='error',
                data=str(e),
            ), 401)
    except Exception as e:
        return make_response(jsonify(
            message='error',
            data=str(e),
        ), 400)

@client_bp.route('/client', methods=['POST'])
def create_client():
    try:
        data = request.json
        client_data = client.create(data)

        auth_payload = {
            'client_id': client_data['client_id'],
            'credential': data['email'],
            'type': 'email',
        }

        try:
            auth = AuthInterface().create_auth_service(auth_payload)
        
        except Exception as e:
            return make_response(jsonify(
                message='error',
                data=str(e),
            ), 400)
        
        return make_response(jsonify(
            message = 'client',
            data = client_data
        ))
    except Exception as e:
        return make_response(jsonify(
            message='error',
            data=str(e),
        ), 400)

@client_bp.route('/client/login/otp', methods=['POST'])
def login_request():
    data = request.json

    try:
        data = client.get_by_client_email(data['email'])

        if not data:
            return make_response(jsonify(
                message='error',
                data=str('CLIENT NOT FOUND'),
            ), 404)
        
        otp_code = AuthInterface().create_otp(data['email'])
        
        return otp_code
    
    except Exception as e:
        otp_code = AuthInterface().create_otp(data['email'])
        return make_response(jsonify(
            message='error',
            data=str('e'),
        ), 400)

@client_bp.route('/client/login/otp/validate', methods=['POST'])
def login_validation():
    data = request.json

    try:
        client_data = client.get_by_client_email(data['email'])

        if not client_data:
            return make_response(jsonify(
                message='error',
                data=str('CLIENT NOT FOUND'),
            ), 404)
        
        otp_validation = AuthInterface().validate_otp(data['email'], data['code'])
        
        return otp_validation
    
    except Exception as e:    
        return make_response(jsonify(
            message='error',
            data=str('e'),
        ), 400)
    
