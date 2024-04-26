# models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from database import engine
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)


# Create database tables
Base.metadata.create_all(bind=engine)
