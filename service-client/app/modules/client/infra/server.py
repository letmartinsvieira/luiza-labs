import sys
# sys.path.append("..")
import json
# import uuid
import logging
from csv import excel
from dataclasses import asdict

import grpc
from marshmallow import ValidationError

from app.grpc.src.client_pb2 import (
    GetClientRequest,
    GetClientResponse,
    CreateClientRequest,
    CreateClientResponse,
    GetClientByEmailRequest,
    UpdateClientResponse,
    UpdateClientRequest,
    DeleteClientRequest,
    DeleteClientResponse,
)
from app.grpc.src.client_pb2_grpc import ClientServicer
from app.modules.client.applcation.exceptions import ClientNotFoundException, ClientEmailAlreadyExistException
from app.modules.client.applcation.use_case.get_client import GetClientUseCaseInput, GetClientUseCase
from app.utils.load_protobuf_payload import load_to_dict
from app.modules.client.infra.schemas_validation.schemas import (
    GetClientSchema,
    CreateClientSchema,
    GetClientByEmailSchema,
    UpdateClientSchema,
    DeleteClientSchema,
)
from app.modules.client.applcation.use_case.create_client import CreateClientUseCase, CreateClientUseCaseInput
from app.modules.client.applcation.use_case.update_client import UpdateClientUseCase, UpdateClientUseCaseInput
from app.modules.client.applcation.use_case.delete_client import DeleteClientUseCase, DeleteClientUseCaseInput
from app.modules.client.infra.db.client_repository import ClientRepository

class ClientServer(ClientServicer):

    def GetClient(
        self,
        request: GetClientRequest,
        context: grpc.ServicerContext,
    ) -> GetClientResponse:

        response = GetClientResponse()
        payload = load_to_dict(request)

        try:
            payload = GetClientSchema().load(payload)

            input_data = GetClientUseCaseInput(
                client_id=payload['client_id'],
            )

            use_case = GetClientUseCase(
                client_repository=ClientRepository(),
            )

            output = use_case.execute(input_data)
            response_data = {
                'name': output.client.name,
                'email': output.client.email,
                'client_id': output.client.id,
            }

            response = GetClientResponse(**response_data)

            context.set_code(grpc.StatusCode.OK)
            return response
        except ValidationError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(json.dumps(e.messages))
        except ClientNotFoundException as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(e.message)
        except Exception as e:
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(e))
        finally:
            return response
        
    
    def GetClientByEmail(
        self,
        request: GetClientByEmailRequest,
        context: grpc.ServicerContext,
    ) -> GetClientResponse:

        response = GetClientResponse()
        payload = load_to_dict(request)

        try:
            payload = GetClientByEmailSchema().load(payload)

            input_data = GetClientUseCaseInput(
                email=payload['email'],
            )

            use_case = GetClientUseCase(
                client_repository=ClientRepository(),
            )

            output = use_case.execute(input_data)
            response_data = {
                'name': output.client.name,
                'email': output.client.email,
                'client_id': output.client.id,
            }

            response = GetClientResponse(**response_data)

            context.set_code(grpc.StatusCode.OK)
            return response
        except ValidationError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(json.dumps(e.messages))
        except ClientNotFoundException as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(e.message)
        except Exception as e:
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(e))
        finally:
            return response


    def CreateClient(
        self,
        request: CreateClientRequest,
        context: grpc.ServicerContext,
    ) -> CreateClientResponse:
        payload = load_to_dict(request)
        response = CreateClientResponse()
        try:
            payload = CreateClientSchema().load(payload)

            input_data = CreateClientUseCaseInput(
                name=payload['name'],
                email=payload['email'],
            )

            use_case = CreateClientUseCase(
                client_repository=ClientRepository(),
            )

            output = use_case.execute(input_data)

            context.set_code(grpc.StatusCode.OK)
            response = CreateClientResponse(**asdict(output))

            return response
        except ValidationError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(json.dumps(e.messages))
        except ClientEmailAlreadyExistException as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(e.message)
        except Exception as e:
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(e))
        finally:
            return response
    

    def UpdateClient(
        self,
        request: UpdateClientRequest,
        context: grpc.ServicerContext,
    ) -> UpdateClientResponse:
        payload = load_to_dict(request)
        response = UpdateClientResponse()
        try:
            payload = UpdateClientSchema().load(payload)

            input_data = UpdateClientUseCaseInput(
                client_id=payload['client_id'],
                name=payload['name'],
                email=payload['email'],
            )

            use_case = UpdateClientUseCase(
                client_repository=ClientRepository(),
            )

            output = use_case.execute(input_data)

            response_data = {
                'name': output.client.name,
                'email': output.client.email,
                'client_id': output.client.id,
            }

            context.set_code(grpc.StatusCode.OK)
            response = UpdateClientResponse(**response_data)

            return response
        except ValidationError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(json.dumps(e.messages))
        except ClientEmailAlreadyExistException as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(e.message)
        except Exception as e:
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(e))
        finally:
            return response
        
    

    def DeleteClient(
        self,
        request: DeleteClientRequest,
        context: grpc.ServicerContext,
    ) -> DeleteClientResponse:
        payload = load_to_dict(request)
        response = DeleteClientResponse()
        try:
            payload = DeleteClientSchema().load(payload)

            input_data = DeleteClientUseCaseInput(
                client_id=payload['client_id'],
            )

            use_case = DeleteClientUseCase(
                client_repository=ClientRepository(),
            )

            output = use_case.execute(input_data)
            output = {'message': 'ok'}
            context.set_code(grpc.StatusCode.OK)
            response = DeleteClientResponse(**asdict(output))

            return response
        except ValidationError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(json.dumps(e.messages))
        except ClientEmailAlreadyExistException as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(e.message)
        except Exception as e:
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(e))
        finally:
            return response