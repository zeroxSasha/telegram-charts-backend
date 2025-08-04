from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Text, Numeric, TIMESTAMP, ForeignKey, func

class Base(DeclarativeBase):
    pass

class Pack(Base):
    __tablename__ = "packs"
    collection_id = Column(Integer, primary_key=True)
    name = Column(Text)
    supply = Column(Integer)

class Activity(Base):
    __tablename__ = "activity"
    id = Column(Integer, primary_key=True, autoincrement=True)
    collection_id = Column(Integer, ForeignKey('packs.collection_id'), nullable=False)
    time = Column(TIMESTAMP, nullable=False, server_default=func.now())
    price = Column(Numeric(10, 2))
