from sqlalchemy import Column, Integer, String, DateTime, func
from app.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(255), unique=True, nullable=False)
    address = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=func.now())
