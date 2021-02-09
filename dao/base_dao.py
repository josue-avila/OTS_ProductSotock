from models.stock import Stock
from dao.session import Session


class BaseDao:
    def __init__(self, type_model):
        self.__type_model = type_model

    def save(self, model: Stock) -> Stock:
        with Session() as s:
            s.add(model)
            s.commit()
            s.refresh(model)
            return model
    
    def read_by_sku(self, sku: str) -> Stock:
        with Session() as s:
            result = s.query(self.__type_model).filter_by(sku=sku).first()
        return result

    def read_all(self) -> list:
        with Session() as s:
            result = s.query(self.__type_model).all()
        return result

    def read_by_seller(self, id_seller: int) -> Stock:
        with Session() as s:
            result = s.query(self.__type_model).filter_by(id_seller=id_seller).all()
        return result
            
    def delete(self, model: Stock) -> None:
        with Session() as s:
            result = s.delete(model)
            s.commit()
