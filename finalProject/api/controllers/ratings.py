from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.ratings import Rating
from ..schemas.ratings import RatingCreate, RatingUpdate


def create_rating(db: Session, rating: RatingCreate):
    db_rating = Rating(**rating.dict())

    db.add(db_rating)

    db.commit()

    db.refresh(db_rating)

    return db_rating


def get_rating(db: Session, rating_id: int):
    db_rating = db.query(Rating).filter(Rating.id == rating_id).first()

    if not db_rating:
        raise HTTPException(status_code=404, detail="Rating not found")

    return db_rating


def update_rating(db: Session, rating_id: int, rating_update: RatingUpdate):
    db_rating = db.query(Rating).filter(Rating.id == rating_id).first()

    if not db_rating:
        raise HTTPException(status_code=404, detail="Rating not found")

    for field, value in rating_update.dict(exclude_unset=True).items():
        setattr(db_rating, field, value)

    db.commit()

    return db_rating
