from dataclasses import asdict

from flask import Blueprint, make_response, jsonify, request

from app.modules.product.application.exceptions import ProductNotFoundException
from app.modules.product.application.use_cases.get_product import GetProductUseCase, GetProductUseCaseInput
from app.modules.product.application.use_cases.list_products import ListProductsUseCase, ListProductsUseCaseInput
from app.modules.product.infra.db.memory_product_repository import MemoryProductRepository

product_bp = Blueprint("product", __name__)

@product_bp.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        use_case = GetProductUseCase(
            MemoryProductRepository(),
        )

        input_data = GetProductUseCaseInput(
            product_id=product_id,
        )

        output = use_case.execute(input_data)

        return make_response(jsonify(
            message="product",
            data={'product': asdict(output.product)},
        ))
    except ProductNotFoundException as e:
        return make_response(jsonify(
            message="error",
            data=str(e),
        ), 404)
    except Exception as e:
        return make_response(jsonify(
            message="error",
            data=str(e),
        ), 400)

@product_bp.route('/products', methods=['GET'])
def list_products():
    try:
        page = request.args.get('page', 1)
        limit = request.args.get('limit', 5)

        use_case = ListProductsUseCase(
            MemoryProductRepository(),
        )

        input_data = ListProductsUseCaseInput(
            page=int(page),
            limit=int(limit),
        )

        output = use_case.execute(input_data)

        return make_response(jsonify(
            message="product",
            data={'products': [asdict(product) for product in output.products]},
        ))
    except Exception as e:
        return make_response(jsonify(
            message="error",
            data=str(e),
        ), 400)