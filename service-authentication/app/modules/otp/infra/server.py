import sys
import json
import logging
from csv import excel
from dataclasses import asdict

import grpc
from marshmallow import ValidationError

from app.grpc.src.otp_pb2 import (
    CreateOTPRequest,
    CreateOTPResponse,
    GetOTPRequest,
    GetOTPResponse,
    GetOTPByCodeRequest,
    GetOTPByCodeResponse,
    ValidateOTPRequest,
    ValidateOTPResponse,
)
from app.grpc.src.otp_pb2_grpc import OTPServicer
from app.modules.otp.applcation.exceptions import OTPNotFoundException, OTPEmailAlreadyExistException
from app.modules.otp.applcation.use_case.get_otp import GetOTPUseCaseInput, GetOTPUseCase
from app.utils.load_protobuf_payload import load_to_dict
from app.modules.otp.infra.schemas_validation.schemas import (
    GetOTPSchema,
    GetOTPByCodeSchema,
    CreateOTPSchema,
    UpdateOTPSchema,
)
from app.modules.otp.applcation.use_case.create_otp import CreateOTPUseCase, CreateOTPUseCaseInput
from app.modules.otp.applcation.use_case.update_otp import UpdateOTPUseCase, UpdateOTPUseCaseInput
from app.modules.otp.infra.db.otp_repository import OTPRepository
from app.modules.auth.infra.db.auth_repository import AuthRepository

class OTPServer(OTPServicer):

    def GetOTP(
        self,
        request: GetOTPRequest,
        context: grpc.ServicerContext,
    ) -> GetOTPResponse:

        response = GetOTPResponse()
        payload = load_to_dict(request)

        try:
            payload = GetOTPSchema().load(payload)

            input_data = GetOTPUseCaseInput(
                id=payload['id'],
            )

            use_case = GetOTPUseCase(
                otp_repository=OTPRepository(),
            )

            output = use_case.execute(input_data)
            response_data = {
                'id': output.otp.id,
                'auth_id': output.otp.auth_id,
                'code': output.otp.code,
                'token': output.otp.token,
            }

            response = GetOTPResponse(**response_data)

            context.set_code(grpc.StatusCode.OK)
            return response
        except ValidationError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(json.dumps(e.messages))
        except OTPNotFoundException as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(e.message)
        except Exception as e:
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(e))
        finally:
            return response


    def GetOTPByCode(
        self,
        request: GetOTPByCodeRequest,
        context: grpc.ServicerContext,
    ) -> GetOTPByCodeResponse:

        response = GetOTPByCodeResponse()
        payload = load_to_dict(request)

        try:
            payload = GetOTPByCodeSchema().load(payload)

            input_data = GetOTPUseCaseInput(
                code=payload['code'],
            )

            use_case = GetOTPUseCase(
                otp_repository=OTPRepository(),
            )

            output = use_case.execute(input_data)
            response_data = {
                'id': output.otp.id,
                'auth_id': output.otp.auth_id,
                'code': output.otp.code,
                'token': output.otp.token,
            }

            response = GetOTPByCodeResponse(**response_data)

            context.set_code(grpc.StatusCode.OK)
            return response
        except ValidationError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(json.dumps(e.messages))
        except OTPNotFoundException as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(e.message)
        except Exception as e:
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(e))
        finally:
            return response


    def CreateOTP(
        self,
        request: CreateOTPRequest,
        context: grpc.ServicerContext,
    ) -> CreateOTPResponse:
        payload = load_to_dict(request)
        response = CreateOTPResponse()
        try:
            payload = CreateOTPSchema().load(payload)

            input_data = CreateOTPUseCaseInput(
                credential=payload['credential'],
            )

            use_case = CreateOTPUseCase(
                otp_repository=OTPRepository(),
                auth_repository=AuthRepository(),
            )

            output = use_case.execute(input_data)

            context.set_code(grpc.StatusCode.OK)
            response = CreateOTPResponse(**asdict(output))

            return response
        except ValidationError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(json.dumps(e.messages))
        except OTPEmailAlreadyExistException as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(e.message)
        except Exception as e:
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(e))
        finally:
            return response


    def ValidateOTP(
            self,
            request: ValidateOTPRequest,
            context: grpc.ServicerContext,
    ) -> ValidateOTPResponse:
        
        response = ValidateOTPResponse()
        payload = load_to_dict(request)

        try:
            payload = UpdateOTPSchema().load(payload)

            input_data = UpdateOTPUseCaseInput(
                code=payload['code']
            )

            use_case = UpdateOTPUseCase(
                otp_repository=OTPRepository(),
                auth_repository=AuthRepository(),
            )

            output = use_case.execute(input_data)

            response_data = {
                'id': output.otp.id,
                'auth_id': output.otp.auth_id,
                'code': output.otp.code,
                'token': output.otp.token,
            }

            context.set_code(grpc.StatusCode.OK)
            response = ValidateOTPResponse(**response_data)

            return response
        except ValidationError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(json.dumps(e.messages))
        except OTPEmailAlreadyExistException as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(e.message)
        except Exception as e:
            context.set_code(grpc.StatusCode.UNKNOWN)
            raise e
        # finally:
        #     return response