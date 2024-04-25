from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..controllers.ratings import create_rating, get_rating, update_rating
from ..schemas.ratings import RatingCreate, RatingResponse, RatingUpdate

router = APIRouter()

@router.post("/ratings/", response_model=RatingResponse)
def create_rating_endpoint(rating_request: RatingCreate, db: Session = Depends(get_db)):
    customer_id = 1
    return create_rating(db=db, rating=rating_request, customer_id=customer_id)

@router.get("/ratings/{rating_id}", response_model=RatingResponse)
def read_rating_endpoint(rating_id: int, db: Session = Depends(get_db)):
    return get_rating(db=db, rating_id=rating_id)

@router.put("/ratings/{rating_id}", response_model=RatingResponse)
def update_rating_endpoint(rating_id: int, rating_update: RatingUpdate, db: Session = Depends(get_db)):
    return update_rating(db=db, rating_id=rating_id, rating_update=rating_update)
