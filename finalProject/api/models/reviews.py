from sqlalchemy import Column, ForeignKey, Integer, String, Float, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    review_text = Column(String(300))
    review_score = Column(Float, index=True, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'))

    customers = relationship('Customer', back_populates="reviews")
