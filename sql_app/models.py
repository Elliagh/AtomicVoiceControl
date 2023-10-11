from datetime import datetime

import sqlalchemy
from sqlalchemy import ForeignKey, Column, Integer, String, TIMESTAMP, PrimaryKeyConstraint
from sql_app.database import Base

metadata = Base.metadata


# TODO продумать логику many-to-many (users-cars)
# TODO сделать валидацию (location, car_type[может enum есть])
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True)
    firstname = Column(String)
    secondname = Column(String)
    location = Column(String)
    email = Column(String)
    address = Column(String)
    number = Column(Integer)
    car_id = Column(Integer, ForeignKey("cars.id"))


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
    user_id = Column(Integer, ForeignKey("users.id"))
    sign = Column(String)
    battery = Column(Integer)
    type = Column(String)
