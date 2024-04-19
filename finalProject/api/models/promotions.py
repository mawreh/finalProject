from sqlalchemy import Column, ForeignKey, Integer, String, Float, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = 'promotions'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promotion_code = Column(String(300))
    expiration_date = Column(DATETIME, index=True, nullable=False, server_default=str(datetime.now()))
