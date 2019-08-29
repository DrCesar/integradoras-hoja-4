
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship

# from db import session

from resources.base import Base
from resources.invoice import invoice_product_table

class Product(Base):
    __tablename__ = 'product'

    id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Numeric)
    date = Column(String)

    invoices = relationship('Invoice', secondary=invoice_product_table, back_populates='products')


    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(cls).filter(cls.id = id).first()


    def __repr__(self):
        return "<Product (id='%s', name='%s', description='%s', price='%s', date='%s')>" % (self.id, self.name, self.description, self.price, self.date)