from datetime import datetime

from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column

metadata = MetaData()

#TODO many to many, location converter
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("firstname", String),
    Column("secondname", String),
    Column("location", String, nullable=False),
    Column("email", String, nullable=False),
    Column("address", String),
    Column("number", Integer),
    Column("car_id", Integer, ForeignKey("cars.id"))
)

cars = Table(
    "cars",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("location", String, nullable=False),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("sign", String),
    Column("Battery", Integer),
    Column("Type", String)
)

register = Table(
    "register",
    metadata,
    Column("token", String),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("password", String, nullable=False),
    Column("last_registration", TIMESTAMP, default=datetime.utcnow),
)