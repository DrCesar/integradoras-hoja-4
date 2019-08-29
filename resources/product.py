
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship

from resources.base import Base
from resources.invoice import invoice_product_table

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Numeric)
    date = Column(String)

    invoices = relationship('Invoice', secondary=invoice_product_table, back_populates='products')



    @classmethod
    def get_all(cls):
        return cls.query.all()