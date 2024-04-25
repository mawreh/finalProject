from sqlalchemy import Column, Integer, String
from ..dependencies.database import Base

class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, index=True)
    rating = Column(Integer)
    feedback = Column(String)
