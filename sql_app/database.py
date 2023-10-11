
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
User_Name = "postgres"
Db_Name = "hackatonspby"
Port = 5432
Password = "postgres"
Host = "localhost"

SQLALCHEMY_DATABASE_URL = f"postgresql://{User_Name}:{Password}@{Host}:{Port}/{Db_Name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()