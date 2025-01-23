import grpc

from app.utils.load_protobuf_payload import load_to_dict
import app.grpc.src.client_pb2 as client_pb2
import app.grpc.src.client_pb2_grpc as client_pb2_grpc
import app.grpc.src.favorite_product_pb2 as product_pb2
import app.grpc.src.favorite_product_pb2_grpc as product_pb2_grpc


class Client:
    
    def __init__(self):
        self.channel = grpc.insecure_channel('test_service_client:5021')
        self.client = client_pb2_grpc.ClientStub(self.channel)
        self.favorite = product_pb2_grpc.FavoriteProductStub(self.channel)
    
    def get_by_client_id(self, id):
        response = self.client.GetClient(client_pb2.GetClientRequest(client_id=id))

        return load_to_dict(response)
    
    def get_by_client_email(self, email):
        try:
            response = self.client.GetClientByEmail(client_pb2.GetClientByEmailRequest(email=email))
            return load_to_dict(response)
        except Exception as e:
            raise e

    def create(self, data):
        payload = client_pb2.CreateClientRequest(
            name=data['name'],
            email=data['email']
        )

        client_data = load_to_dict(self.client.CreateClient(payload))

        return client_data
    
    def favorite_product(self, product_id, client_id):
        payload = product_pb2.CreateFavoriteProductRequest(
            client_id=client_id,
            product_id=product_id
        )

        favorite = load_to_dict(self.favorite.CreateFavoriteProduct(payload))

        return favorite

    def update_client(self, data, client_id):
        payload = client_pb2.UpdateClientRequest(
            client_id=client_id,
            name=data['name'],
            email=data['email']
        )

        request = load_to_dict(self.client.UpdateClient(payload))

        return request
