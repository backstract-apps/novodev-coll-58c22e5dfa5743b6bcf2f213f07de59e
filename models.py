from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    user_id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    password = Column(String, primary_key=False)
    role = Column(String, primary_key=False)

