from dao.base_dao import BaseDao
from models.stock import Stock

class StockDao(BaseDao):
    def __init__(self):
        super().__init__(Stock)