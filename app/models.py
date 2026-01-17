from sqlalchemy import Column, Integer, String, Float
from .database import Base

class RawData(Base):
    __tablename__ = "raw_data"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Float)
    salary = Column(Float)


class CleanedData(Base):
    __tablename__ = "cleaned_data"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    salary = Column(Float)
