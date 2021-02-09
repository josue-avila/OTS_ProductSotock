# import sys
# sys.path.append('.')

# from models.stock import Stock
# import pytest


# class TestStockModel:
#     sku = 'TEST-STO-50-CK'
#     quantity = 3
#     id_product = 20
#     id_seller = 10

#     def test_instance(self):
#         stock = Sotck(self.sku, self.quantity, self.id_product, self.id_seller)
#         assert isinstance(stock, Stock)
    
#     def test_empty_sku(self):
#         with pytest.raises(ValueError):
#             stock = Stock("", self.quantity, self.id_product, self.id_seller)
        
#     def test_sku_length(self):
#         with pytest.raises(ValueError):
#             stock = Stock("A" * 51, self.quantity, self.id_product, self.id_seller)
    
#     def test_sku_type(self):
#         with pytest.raises(TypeError):
#             stock = Stock(50, self.quantity, self.id_product, self.id_seller)
     
#     def test_quantity_not_float(self):
#         with pytest.raises(ValueError):
#             stock = Stock(self.sku, 3.14, self.id_product, self.id_seller)
     
#     def test_quantity_type(self):
#         with pytest.raises(TypeError):
#             stock = Stock(self.sku, "3", self.id_product, self.id_seller)

    # def test_id_product_type(self):
    #     with pytest.raises(ValueError):
    #         stock = Stock(self.sku, self.quantity, "50", self.id_seller)

    # def test_id_seller_type(self):
    #     with pytest.raises(ValueError):
    #         stock = Stock(self.sku, self.quantity, self.id_product, "20")
