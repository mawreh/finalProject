from sqlalchemy import Column, ForeignKey, Integer, Float, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    tracking_number = Column(String(300))
    order_status = Column(String(300))
    total_price = Column(Float, index=True, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'))

    order_details = relationship("OrderDetail", back_populates="orders")
    customers = relationship('Customer', back_populates="orders")
