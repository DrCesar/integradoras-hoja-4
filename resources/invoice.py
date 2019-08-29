
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from resources.base import Base

invoice_product_table = Table('association', Base.metadata,
    Column('invoice_id', Integer, ForeignKey('invoice.id')),
    Column('product_id', Integer, ForeignKey('product.id'))
)


class Invoice(Base):
    __tablename__ = 'invoice'

    id = Column(Integer, primary_key=True)
    address = Column(String)
    date_created = Column(Integer)
    name = Column(String)
    nit = Column(String)

    products = relationship('Product', secondary=invoice_product_table, back_populates='invoices')


    @classmethod
    def get_all(cls):
        return cls.query.all()