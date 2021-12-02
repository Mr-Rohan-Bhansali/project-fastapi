from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Integer, String
from .database import Base


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    bookcount = Column(Integer)


class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    issued = Column(Integer, default=0)
    name = Column(String)
    count = Column(Integer, default=0)
    date = Column(DateTime)


class Management(Base):
    __tablename__ = "management"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    ret = Column('return', Boolean, default=False)
    b_id = Column(Integer, ForeignKey('inventory.id'))
    s_id = Column(Integer, ForeignKey('student.id'))

    inventory = relationship('Inventory')
    student = relationship('Student')
