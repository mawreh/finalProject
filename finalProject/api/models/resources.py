from sqlalchemy import Column, ForeignKey, Integer, Float, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ingredient_name = Column(String(100))
    amount = Column(Float, index=True, nullable=False)
    unit = Column(String(300))
