from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base


from coolapi.database.connector import ENGINE


Base = declarative_base()


class Buildings(Base):
    __tablename__ = "buildings"
    id = Column(String, primary_key=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
    max_floors = Column(Integer, nullable=False)


class CroissantsRequests(Base):
    __tablename__ = "croissants_requests"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    requester = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    building = Column(String, ForeignKey(Buildings.id), nullable=False)
    floor = Column(Integer, nullable=False)
    time = Column(DateTime(timezone=True), nullable=False)


def configure_database():
    print("Configuring CoolAPI DB")
    Base.metadata.create_all(ENGINE.engine)
