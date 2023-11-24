from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    category = Column(String)
    supplier = Column(String)
    
    orders = relationship('OrderItem', backref='product')  # Relationship with OrderItem

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    address = Column(String)
    phone_number = Column(String)
    loyalty_points = Column(Integer)
    
    orders = relationship('Order', backref='customer')  # Relationship with Order

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    total_price = Column(Float)
    status = Column(String)

    customer = relationship('Customer', backref='orders')
    items = relationship('OrderItem', backref='order')