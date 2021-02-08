from flask_restful import fields, marshal_with
from models.stock import Stock
from dao.stock_dao import StockDao
from resources.base_resource import BaseResource


class StockResource(BaseResource):
    fields = {
        "sku": fields.String,
        "quantity": fields.Integer,
        "id_product": fields.Integer,
        "id_seller": fields.Integer
    }

    def __init__(self) -> None:
        self.__dao = StockDao()
        self.__model_type = Stock
        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields)
    def get(self, sku=None):
        return super().get(sku)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def put(self, sku: str):
        return super().put(sku)

    @marshal_with(fields)
    def delete(self, sku: str):
        return super().delete(sku)
