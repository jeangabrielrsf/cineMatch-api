from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    image_url = Column(String)
    vote_average = Column(Integer)
    vote_count = Column(Integer)

class Gender(Base):
    __tablename__ = "genders"

    id = Column(Integer, index=True)
    name = Column(String, index=True)
