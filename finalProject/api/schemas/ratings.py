from pydantic import BaseModel
from typing import Optional

class RatingBase(BaseModel):
    rating: int
    feedback: str

class RatingCreate(RatingBase):
    pass

class RatingUpdate(BaseModel):
    rating: Optional[int]
    feedback: Optional[str]

class RatingResponse(RatingBase):
    id: int

    class Config:
        orm_mode = True
