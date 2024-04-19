from sqlalchemy import Column, ForeignKey, Integer, String, Float, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    transaction = Column(String(300))
    payment_type = Column(String(100))
    card_info = Column(String(100))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    customers = relationship('Customer', back_populates="paymentd")
