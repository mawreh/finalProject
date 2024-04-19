from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .customers import Customer

class ReviewBase(BaseModel):
    customer_id: int
    review_text: str
    review_score: float



class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(BaseModel):
    customer_id: Optional[int] = None
    review_text: Optional[str] = None
    review_score: Optional[float] = None


class Review(ReviewBase):
    id: int
    customer: Customer = None

    class ConfigDict:
        from_attributes = True

