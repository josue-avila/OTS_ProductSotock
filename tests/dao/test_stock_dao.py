from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import ProgrammingError, DataError
from dao.stock_dao import StockDao
from models.stock import Stock
from dao.base_dao import BaseDao
import pytest


class TestStockDao:
    @pytest.fixture
    def stock_instance(self):
        item = Stock('stock123', 10, 1, 1)
        return item

    @pytest.fixture
    def stock_dao(self):
        dao = StockDao()
        return dao

    def test_stock_dao_instance(self, stock_dao):
        assert isinstance(stock_dao, StockDao)
        assert isinstance(stock_dao, BaseDao)

    def test_save_method(self, stock_dao, stock_instance):
        stock_instance.sku = '123abc'
        stock_saved = stock_dao.save(stock_instance)
        assert stock_saved.sku == stock_instance.sku
        assert stock_saved.quantity == stock_instance.quantity
        assert stock_saved.id_product == stock_instance.id_product
        assert stock_saved.id_seller == stock_instance.id_seller
        stock_dao.delete(stock_saved)

    @pytest.mark.parametrize("fake_stock", [
        'string', 1, 1.0, [1, 2, 3]
    ])
    def test_fail_save_method(self, stock_dao, fake_stock):
        with pytest.raises(UnmappedInstanceError):
            stock_dao.save(fake_stock)

    def test_read_by_sku_method(self, stock_dao, stock_instance):
        stock_instance.sku = '123abc'
        stock_saved = stock_dao.save(stock_instance)
        stock_read = stock_dao.read_by_sku(stock_saved.sku)
        assert isinstance(stock_read, Stock)
        stock_dao.delete(stock_saved)

    @pytest.mark.parametrize("fake_stock", [
        10, 1.0, [1, 2, 3]
    ])
    def test_fail_read_by_sku_method(self, stock_dao, fake_stock):
        with pytest.raises(ProgrammingError):
            stock_dao.read_by_sku(fake_stock)

    def test_read_by_seller(self, stock_dao, stock_instance):
        stock_instance.sku = '123abc'
        stock_saved = stock_dao.save(stock_instance)
        stock_read = stock_dao.read_by_seller(stock_saved.id_seller)
        assert isinstance(stock_read, list)
        assert all(isinstance(item, Stock) for item in stock_read)
        stock_dao.delete(stock_saved)

    def test_fail_read_by_seller_method(self, stock_dao):
        with pytest.raises(DataError):
            stock_dao.read_by_seller('fake_stock')

    def test_read_all_method(self, stock_dao):
        stock_list = stock_dao.read_all()
        assert isinstance(stock_list, list)
        assert all(isinstance(item, Stock) for item in stock_list)

    def test_delete_method(self, stock_dao, stock_instance):
        stock_instance.sku = '123abc'
        stock_saved = stock_dao.save(stock_instance)
        stock_read = stock_dao.read_by_sku(stock_saved.sku)
        stock_dao.delete(stock_read)
        stock_read = stock_dao.read_by_sku(stock_saved.sku)
        assert stock_read is None

    @pytest.mark.parametrize("fake_stock", [
        'string', 1, 1.0, [1, 2, 3]
    ])
    def test_not_delete(self, stock_dao, fake_stock):
        with pytest.raises(UnmappedInstanceError):
            stock_dao.delete(fake_stock)
