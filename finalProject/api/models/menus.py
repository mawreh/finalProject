from sqlalchemy import Column, ForeignKey, Integer, String, Float, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Menu(Base):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dish_name = Column(String(300))
    ingredients = Column(String(300))
    price = Column(Float, index=True, nullable= False)
    calories = Column(Integer,index=True, nullable = False)
    food_category = Column(String(300))
