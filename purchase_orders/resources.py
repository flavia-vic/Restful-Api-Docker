from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from .services import PurchaseOrdersService
from flasgger import swag_from


class PurchaseOrders(Resource):
    __service__ = PurchaseOrdersService()

    parser = reqparse.RequestParser()
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='Informe uma descrição válida'
    )
    parser.add_argument(
        'quantity',
        type=int,
        required=True,
        help='Informe uma quantidade'
    )

    @jwt_required()
    @swag_from('../docs/purchase_orders/get_purchase_orders.yml') #2
    def get(self):
        return self.__service__.find_all()

    @jwt_required()
    @swag_from('../docs/purchase_orders/create_purchase_order.yml') #1
    def post(self):
        data = PurchaseOrders.parser.parse_args()
        return self.__service__.create(**data)


class PurchaseOrderById(Resource):
    __service__ = PurchaseOrdersService()

    @jwt_required()
    @swag_from('../docs/purchase_orders/purchase_order_by_id.yml') #3
    def get(self, id):
        return self.__service__.find_by_id(id)
    
    @jwt_required()
    @swag_from('../docs/purchase_orders/delete_purchase_order.yml') #4
    def delete(self, id):
        return self.__service__.delete(id)

