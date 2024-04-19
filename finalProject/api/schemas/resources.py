from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ResourceBase(BaseModel):
    ingredient_name: str
    amount: float
    unit: str


class ResourceCreate(ResourceBase):
    pass


class ResourceUpdate(BaseModel):
    ingredient_name: Optional[str] = None
    amount: Optional[float] = None
    unit: Optional[str] = None

class Resource(ResourceBase):
    id: int

    class ConfigDict:
        from_attributes = True
