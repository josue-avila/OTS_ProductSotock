from models.stock import Stock
import pytest


class TestStockModel:
    @pytest.fixture
    def stock_instance(self):
        item = Stock('TEST-STO-50-CK', 3, 20, 10)
        return item

    def test_instance(self, stock_instance):
        assert isinstance(stock_instance, Stock)
    
    def test_empty_sku(self, stock_instance):
        with pytest.raises(ValueError):
            stock_instance.sku = ''
        
    def test_sku_length(self, stock_instance):
        with pytest.raises(ValueError):
            stock_instance.sku = ' '*51
    
    def test_sku_type(self, stock_instance):
        with pytest.raises(TypeError):
            stock_instance.sku = 50

    def test_quantity_type(self, stock_instance):
        with pytest.raises(TypeError):
            stock_instance.quantity = '3'

    def test_quantity_greater_than_zero(self, stock_instance):
        with pytest.raises(ValueError):
            stock_instance.quantity = -5

    def test_id_product_type(self, stock_instance):
        with pytest.raises(TypeError):
            stock_instance.id_product = '50'

    def test_id_product_greater_than_zero(self, stock_instance):
        with pytest.raises(ValueError):
            stock_instance.id_product = -1

    def test_id_seller_type(self, stock_instance):
        with pytest.raises(TypeError):
            stock_instance.id_seller = '20'

    def test_id_seller_greater_than_zero(self, stock_instance):
        with pytest.raises(ValueError):
            stock_instance.id_seller = -1
