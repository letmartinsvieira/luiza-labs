from __future__ import print_function
from dataclasses import asdict
from flask import Flask, Blueprint, make_response, jsonify, request
from os import environ
import grpc
from requests import HTTPError, ReadTimeout, Session, Timeout
from requests.exceptions import SSLError

import app.grpc.src.auth_pb2 as auth_pb2
import app.grpc.src.auth_pb2_grpc as auth_pb2_grpc
from app.utils.load_protobuf_payload import load_to_dict
from app.modules.authentication.application.auth_interface import AuthInterface
from app.utils.middleware.require_authentication import require_authentication


auth_pb = Blueprint('auth', __name__)
auth = AuthInterface()

@auth_pb.route('/auth/<int:client_id>', methods=['GET'])
@require_authentication
def get_auth(client_id):
    try:
        response = auth.get_auth(client_id)
        
        return make_response(jsonify(
            message = 'auth',
            data = load_to_dict(response)
        ))

    except Exception as e:
        return make_response(jsonify(
            message='error',
            data=str(e),
        ), 400)

@auth_pb.route('/auth/<string:email>', methods=['GET'])
@require_authentication
def get_auth_by_email(email):
    try:
        response = auth.get_auth_by_email(email)

        return make_response(jsonify(
            message = 'auth',
            data = response
        ))
    except Exception as e:
        return make_response(jsonify(
            message='error',
            data=str(e),
        ), 400)

@auth_pb.route('/auth', methods=['POST'])
@require_authentication
def create_auth():
    data = request.json

    try:
        response = auth.create_auth_service(data)

        return make_response(jsonify(
            message = 'auth',
            data = response
        ))
    except Exception as e:
        return make_response(jsonify(
            message='error',
            data=str(e),
        ), 400)
