from sqlalchemy import Column, Integer, String, Float
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