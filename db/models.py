from datetime import datetime

import sqlalchemy
from sqlalchemy import ForeignKey, Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True)
    firstname = Column(String)
    secondname = Column(String)
    location = Column(String)
    email = Column(String, unique=True)
    address = Column(String)
    number = Column(Integer)
    cars = relationship("CarsUsers", backref="users")

class Register(Base):
    __tablename__ = "register"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    token = Column(String)
    password = Column(String)
    time = Column(TIMESTAMP, default=datetime.utcnow())


class Cars(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, unique=True)
    location = Column(String)
    sign = Column(String)
    battery = Column(Integer)
    type = Column(String)
    users = relationship("CarsUsers", backref="cars")

class CarsUsers(Base):
    __tablename__ = "carsusers"
    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    car_id = Column(Integer, ForeignKey("cars.id"))