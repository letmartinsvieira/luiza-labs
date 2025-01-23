import json

import grpc
from marshmallow import ValidationError

from app.grpc.src.favorite_product_pb2 import (
    CreateFavoriteProductRequest,
    CreateFavoriteProductResponse,
    ListFavoriteProductRequest,
    ListFavoriteProductResponse,
)
from app.grpc.src.favorite_product_pb2_grpc import FavoriteProductServicer
from app.modules.favorite_product.application.exceptions import (
    ProductNotFoundException,
    FavoriteProductAlreadyExistException,
)
from app.modules.favorite_product.application.use_cases.create_favorite_product import (
    CreateFavoriteProductUseCaseInput,
    CreateFavoriteProductUseCase,
)
from app.modules.favorite_product.application.use_cases.list_favorite_products import (
    ListFavoriteProductUseCaseInput,
    ListFavoriteProductUseCase,
)
from app.modules.favorite_product.infra.api.product_api import ProductApi
from app.modules.favorite_product.infra.db.favorite_product_repository import FavoriteProductRepository
from app.modules.favorite_product.infra.schemas_validation.schemas import CreateFavoriteProductSchema, ListFavoriteProductSchema
from app.utils.load_protobuf_payload import load_to_dict


class FavoriteProductServer(FavoriteProductServicer):

    def ListFavoriteProduct(
        self,
        request: ListFavoriteProductRequest,
        context: grpc.ServicerContext,
    ) -> ListFavoriteProductResponse:
        
        response = ListFavoriteProductResponse()
        payload = load_to_dict(request)

        try:
            payload = ListFavoriteProductSchema().load(payload)

            input_data = ListFavoriteProductUseCaseInput(
                client_id=payload['client_id'],
                page=payload['page'],
                limit=payload['limit']
            )
            use_case = ListFavoriteProductUseCase(
                favorite_product_repository=FavoriteProductRepository(),
            )

            output = use_case.execute(input_data)

            response = ListFavoriteProductResponse(**output)
            return response
        except ValidationError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(json.dumps(e.messages))
        except ProductNotFoundException as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(e.message)
        except FavoriteProductAlreadyExistException as e:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details(e.message)
        except Exception as e:
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(e))
        finally:
            return response


    def CreateFavoriteProduct(
        self,
        request: CreateFavoriteProductRequest,
        context: grpc.ServicerContext,
    ) -> CreateFavoriteProductResponse:
        response = CreateFavoriteProductResponse()
        payload = load_to_dict(request)

        try:
            payload = CreateFavoriteProductSchema().load(payload)

            input_data = CreateFavoriteProductUseCaseInput(
                client_id=payload['client_id'],
                product_id=payload['product_id'],
            )

            use_case = CreateFavoriteProductUseCase(
                product_api=ProductApi(),
                favorite_product_repository=FavoriteProductRepository(),
            )

            output = use_case.execute(input_data)
            response_data = {
                'favorite_product_id': output.favorite_product_id,
            }

            response = CreateFavoriteProductResponse(**response_data)

            context.set_code(grpc.StatusCode.OK)
            return response
        except ValidationError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(json.dumps(e.messages))
        except ProductNotFoundException as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(e.message)
        except FavoriteProductAlreadyExistException as e:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details(e.message)
        except Exception as e:
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(e))
        finally:
            return response