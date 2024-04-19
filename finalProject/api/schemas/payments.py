from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .customers import Customer



class PaymentBase(BaseModel):
    transaction: str
    payment_type: str
    card_info: str
    customer_id: int


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(PaymentBase):
    customer_id: Optional[int] = None
    transaction: Optional[str] = None
    payment_type: Optional[str] = None
    card_info = Optional[str] = None

class Payment(PaymentBase):
    id: int
    customer: Customer = None

    class ConfigDict:
        from_attributes = True
