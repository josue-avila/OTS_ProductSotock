from typing import Type
from flask import request
from flask_restful import Resource
from dao.base_dao import BaseDao
from models.stock import Stock


class BaseResource(Resource):
    def __init__(self, dao: BaseDao, model_type: Type):
        self.__dao = dao
        self.__model_type = model_type

    def get(self, value=None):
        try:
            value = int(value)
            return self.__dao.read_by_seller(value)
        except ValueError:
            if isinstance(value, str):
                return self.__dao.read_by_sku(value)
        except TypeError:
            return self.__dao.read_all()

    def post(self):
        data = request.json
        model = self.__model_type(**data)
        self.__dao.save(model)

        return model, 200

    def put(self, sku: str):
        data = request.json
        if data['sku'] == sku:
            model = self.__dao.read_by_sku(sku)
            for key, value in data.items():
                setattr(model, key, value)
            return self.__dao.save(model)
        return None, 404

    def delete(self, sku: str):
        model = self.__dao.read_by_sku(sku)
        self.__dao.delete(model)
        return None, 204
