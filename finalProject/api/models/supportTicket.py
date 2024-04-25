from sqlalchemy import Column, Integer, String, Text, ForeignKey
from ..dependencies.database import Base

class SupportTicket(Base):
    __tablename__ = 'support_tickets'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    subject = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    status = Column(String(100), default='open')


