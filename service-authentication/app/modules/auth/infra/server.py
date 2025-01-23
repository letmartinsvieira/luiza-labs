import sys
# sys.path.append("..")
import json
# import uuid
import logging
from csv import excel
from dataclasses import asdict

import grpc
from marshmallow import ValidationError

from app.grpc.src.auth_pb2 import (
    GetAuthRequest,
    GetAuthResponse,
    GetAuthByEmailRequest,
    GetAuthByEmailResponse,
    CreateAuthRequest,
    CreateAuthResponse,
)
from app.grpc.src.auth_pb2_grpc import AuthServicer
from app.modules.auth.applcation.exceptions import AuthNotFoundException, AuthEmailAlreadyExistException
from app.modules.auth.applcation.use_case.get_auth import GetAuthUseCaseInput, GetAuthUseCase
from app.utils.load_protobuf_payload import load_to_dict
from app.modules.auth.infra.schemas_validation.schemas import (
    GetAuthSchema,
    CreateAuthSchema,
    GetAuthByEmailSchema,
)
from app.modules.auth.applcation.use_case.create_auth import CreateAuthUseCase, CreateAuthUseCaseInput
from app.modules.auth.infra.db.auth_repository import AuthRepository

class AuthServer(AuthServicer):

    def GetAuth(
        self,
        request: GetAuthRequest,
        context: grpc.ServicerContext,
    ) -> GetAuthResponse:

        response = GetAuthResponse()
        payload = load_to_dict(request)

        try:
            payload = GetAuthSchema().load(payload)

            input_data = GetAuthUseCaseInput(
                client_id=payload['client_id'],
            )

            use_case = GetAuthUseCase(
                auth_repository=AuthRepository(),
            )

            output = use_case.execute(input_data)
            response_data = {
                'id': output.auth.id,
                'type': output.auth.type,
                'credential': output.auth.credential,
                'client_id': output.auth.client_id,
            }

            response = GetAuthResponse(**response_data)

            context.set_code(grpc.StatusCode.OK)
            return response
        except ValidationError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(json.dumps(e.messages))
        except AuthNotFoundException as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(e.message)
        except Exception as e:
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(e))
        finally:
            return response


    def GetAuthByEmail(
        self,
        request: GetAuthByEmailRequest,
        context: grpc.ServicerContext,
    ) -> GetAuthByEmailResponse:

        response = GetAuthByEmailResponse()
        payload = load_to_dict(request)

        try:
            payload = GetAuthByEmailSchema().load(payload)

            input_data = GetAuthUseCaseInput(
                credential=payload['email'],
            )

            use_case = GetAuthUseCase(
                auth_repository=AuthRepository(),
            )

            output = use_case.execute(input_data)
            response_data = {
                'id': output.auth.id,
                'type': output.auth.type,
                'credential': output.auth.credential,
                'client_id': output.auth.client_id,
            }

            response = GetAuthByEmailResponse(**response_data)

            context.set_code(grpc.StatusCode.OK)
            return response
        except ValidationError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(json.dumps(e.messages))
        except AuthNotFoundException as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(e.message)
        except Exception as e:
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(e))
        finally:
            return response

    def CreateAuth(
        self,
        request: CreateAuthRequest,
        context: grpc.ServicerContext,
    ) -> CreateAuthResponse:
        payload = load_to_dict(request)
        response = CreateAuthResponse()
        try:
            payload = CreateAuthSchema().load(payload)

            input_data = CreateAuthUseCaseInput(
                type=payload['type'],
                credential=payload['credential'],
                client_id=payload['client_id']
            )

            use_case = CreateAuthUseCase(
                auth_repository=AuthRepository(),
            )

            output = use_case.execute(input_data)

            context.set_code(grpc.StatusCode.OK)
            response = CreateAuthResponse(**asdict(output))

            return response
        except ValidationError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(json.dumps(e.messages))
        except AuthEmailAlreadyExistException as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(e.message)
        except Exception as e:
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(e))
        # finally:
        #     return response