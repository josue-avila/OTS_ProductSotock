from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Stock(Base):
    __tablename__ = "stock"
    sku = Column(String(length=50), primary_key=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    id_product = Column(Integer, nullable=False)
    id_seller = Column(Integer, nullable=False)

    def __init__(self, sku: str, quantity: int, id_seller: int, id_product: int) -> None:
        self.sku = sku
        self.quantity = quantity
        self.id_product = id_product
        self.id_seller = id_seller
    
    @validates('sku')
    def validate_sku(self, key, sku):
        if not isinstance(sku, str):
            raise TypeError('SKU must be a string')
        if not sku.strip():
            raise ValueError('SKU must not be empty')
        if len(sku) > 50:
            raise ValueError("SKU can't be more than 50 characters")
        return sku

    @validates('quantity')
    def validate_quantity(self, key, quantity):
        if not isinstance(quantity, int):
            raise TypeError('Quantity must be a valid number')
        if quantity < 0:
            raise ValueError("Quantity can't be smaller than 0 (zero)")
        return quantity

    @validates('id_product')
    def validate_id_product(self, key, id_product):
        if not isinstance(id_product, int):
            raise TypeError('id_product must be a valid number')
        if id_product < 0:
            raise ValueError("id_product can't be smaller than 0 (zero)")
        return id_product

    @validates('id_seller')
    def validate_id_seller(self, key, id_seller):
        if not isinstance(id_seller, int):
            raise TypeError('id_seller must be a valid number')
        if id_seller < 0:
            raise ValueError("id_seller can't be smaller than 0 (zero)")
        return id_seller
