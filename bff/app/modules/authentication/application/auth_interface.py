import grpc
import app.grpc.src.auth_pb2 as auth_pb2
import app.grpc.src.auth_pb2_grpc as auth_pb2_grpc
import app.grpc.src.otp_pb2 as otp_pb2
import app.grpc.src.otp_pb2_grpc as otp_pb2_grpc
from app.utils.load_protobuf_payload import load_to_dict


class AuthInterface:
    def __init__(self):
        self.channel = grpc.insecure_channel('test_service_authentication:5022')
        self.auth_client = auth_pb2_grpc.AuthStub(self.channel)
        self.otp_client = otp_pb2_grpc.OTPStub(self.channel)

    def create_auth_service(self, data):

        payload = auth_pb2.CreateAuthRequest(
            client_id=data['client_id'],
            credential=str(data['credential']),
            type=str(data['type']),
        )

        response = load_to_dict(self.auth_client.CreateAuth(payload))
        return response

    def get_auth(self, client_id):
        try:
            response = self.auth_client.GetAuth(auth_pb2.GetAuthRequest(client_id=client_id))

            return response

        except Exception as e:
            return e
    
    def get_auth_by_email(self, email):
        try:
            response = self.auth_client.GetAuthByEmail(
                auth_pb2.GetAuthByEmailRequest(email=email)
            )
            return load_to_dict(response)

        except Exception as e:
            return e
    
    def create_otp(self, email):
        try:
            request = otp_pb2.CreateOTPRequest(credential=email)
            response = load_to_dict(self.otp_client.CreateOTP(request))
            return response
        except Exception as e:
            return e
    
    def validate_otp(self, credential, code):
        try:
            request = otp_pb2.ValidateOTPRequest(
                code=code,
                credential=credential
            )
            response = load_to_dict(self.otp_client.ValidateOTP(request))
            return response
        except Exception as e:
            return e