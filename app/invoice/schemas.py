from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from pydantic import Field
class InvoiceItemRequest(BaseModel):
    product_name: str
    quantity: int
    unit_price: float

class InvoiceRequest(BaseModel):
    customer_name: Optional[str] = Field(default="Anonymous")
    customer_phone: Optional[str] = Field(default="1234567890")
    items: List[InvoiceItemRequest]

#########################################

class InvoiceItemCreate(BaseModel):
    product_name: str
    quantity: int
    unit_price: float
    total_price: float

class InvoiceCreate(BaseModel):
    customer_id: int
    items: List[InvoiceItemCreate]
    total_amount: float
    payment_method: str

class InvoiceItemResponse(BaseModel):
    id: int
    product_name: str
    quantity: int
    unit_price: float
    total_price: float

    class Config:
        orm_mode = True

class InvoiceResponse(BaseModel):
    id: int
    invoice_number: str
    customer_id: int
    total_amount: float
    payment_method: str
    status: str
    created_at: datetime
    items: List[InvoiceItemResponse]

    class Config:
        orm_mode = True