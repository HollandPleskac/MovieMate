import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base, sessionmaker

# Load environment variables from .env file
load_dotenv()

# Retrieve variables from environment
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    email = Column("email", String, primary_key=True)

    def __init__(self, email):
        self.email = email

    # for printing User objects
    def __repr__(self):
        return f"{self.email}"

class Movie(Base):
    __tablename__ = "movies"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name",String, nullable=False)
    description = Column("description", String, nullable=False)
    imageUrl = Column("imageUrl", String, nullable=False)

    # owner = Column(Integer, ForeignKey("people.ssn"))

    