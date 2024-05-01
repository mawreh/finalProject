from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CustomerBase(BaseModel):
    customer_name: str
    customer_email: str
    customer_address: str
    customer_phone: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(CustomerBase):
    customer_name: Optional[str] = None
    customer_email: Optional[str] = None
    customer_address: Optional[str] = None
    customer_phone: Optional[str] = None

class Customer(CustomerBase):
    id: int

    class ConfigDict:
        from_attributes = True
