# from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
# from app.database import Base
# from datetime import datetime  # Correct import
# from sqlalchemy.orm import relationship

# class Invoice(Base):
#     _tablename_ = "invoices"

#     id = Column(Integer, primary_key=True, index=True)
#     customer_name = Column(String, nullable=False, default="Anonymous")
#     customer_phone = Column(String, nullable=False, default="1234567890")
#     total_amount = Column(Float, nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)  # Corrected

#     # Relationship to invoice items
#     items = relationship("InvoiceItem", back_populates="invoice")

# class InvoiceItem(Base):
#     _tablename_ = "invoice_items"

#     id = Column(Integer, primary_key=True, index=True)
#     invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False)
#     product_name = Column(String, nullable=False)
#     quantity = Column(Integer, nullable=False)
#     unit_price = Column(Float, nullable=False)
#     total_price = Column(Float, nullable=False)  # quantity * unit_price

#     invoice = relationship("Invoice", back_populates="items")

from typing import List
from pydantic import BaseModel
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base
from datetime import datetime  # Correct import
from sqlalchemy.orm import relationship

# class Invoice(Base):
#     _tablename_ = "invoices"

#     id = Column(Integer, primary_key=True, index=True)
#     invoice_number = Column(String, unique=True, nullable=False)
#     customer_id = Column(Integer, ForeignKey("customers.id"))
#     total_amount = Column(Float)
#     payment_method = Column(String)
#     status = Column(String, default="PAID")
#     created_at = Column(DateTime(timezone=True), server_default=func.now())

#     # Relationship to invoice items
#     items = relationship("InvoiceItem", back_populates="invoice")

# class InvoiceItem(Base):
#     _tablename_ = "invoice_items"

#     id = Column(Integer, primary_key=True, index=True)
#     invoice_id = Column(Integer, ForeignKey("invoices.id"))
#     product_name = Column(String)
#     quantity = Column(Integer)
#     unit_price = Column(Float)
#     total_price = Column(Float)

#     invoice = relationship("Invoice", back_populates="items")


# class Invoice(Base):
#     _tablename_ = "invoices"

#     id = Column(Integer, primary_key=True, index=True)
#     customer_name = Column(String)  # Make sure these column names match exactly
#     customer_phone = Column(String)
#     total_amount = Column(Float)
#     payment_method = Column(String)
#     created_at = Column(DateTime, default=datetime.utcnow)

#     items = relationship("InvoiceItem", back_populates="invoice")

#     def _init_(self, **kwargs):
#         for key, value in kwargs.items():
#             setattr(self, key, value)

# class InvoiceItem(Base):
#     _tablename_ = "invoice_items"

#     id = Column(Integer, primary_key=True, index=True)
#     invoice_id = Column(Integer, ForeignKey("invoices.id"))
#     product_name = Column(String)
#     quantity = Column(Integer)
#     unit_price = Column(Float)
#     total_price = Column(Float)

#     invoice = relationship("Invoice", back_populates="items")

# class Invoice(Base):
#     _tablename_ = "invoices"

#     id = Column(Integer, primary_key=True, index=True)
#     customer_name = Column(String)
#     customer_phone_invoice_number = Column(String)  # Updated to match your column name
#     total_amount = Column(Float)
#     created_at = Column(DateTime, default=datetime.utcnow)

#     items = relationship("InvoiceItem", back_populates="invoice")


from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    customer_phone = Column(String)  # Changed from customer_phone_invoice_number
    invoice_number = Column(String)  # Added this column
    total_amount = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    items = relationship("InvoiceItem", back_populates="invoice")

class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    product_name = Column(String)
    quantity = Column(Integer)
    unit_price = Column(Float)
    total_price = Column(Float)

    invoice = relationship("Invoice", back_populates="items")




# from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
# from sqlalchemy.sql import func
# from app.database import Base
# from datetime import datetime  # Correct import
# from sqlalchemy.orm import relationship

# class Invoice(Base):
#     __tablename__ = "invoices"

#     id = Column(Integer, primary_key=True, index=True)
#     invoice_number = Column(String(255), unique=True)
#     customer_id = Column(Integer, ForeignKey("customers.id"))
#     total_amount = Column(Float)
#     payment_method = Column(String(255))
#     status = Column(String(255), default="PAID")
#     created_at = Column(DateTime(timezone=True), server_default=func.now())

#     # Relationship to invoice items
#     items = relationship("InvoiceItem", back_populates="invoice")

# class InvoiceItem(Base):
#     __tablename__ = "invoice_items"

#     id = Column(Integer, primary_key=True, index=True)
#     invoice_id = Column(Integer, ForeignKey("invoices.id"))
#     product_name = Column(String(255))
#     quantity = Column(Integer)
#     unit_price = Column(Float)
#     total_price = Column(Float)

#     invoice = relationship("Invoice", back_populates="items")



