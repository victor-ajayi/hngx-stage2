from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from app import models, schemas
from app.models import User

from .database import get_db

router = APIRouter(prefix="/api")


@router.post("/", status_code=201)
def create_user(
    user_create: schemas.UserCreate, db: Session = Depends(get_db)
) -> schemas.User:
    user = db.query(User).filter_by(name=user_create.name).first()
    if user:
        raise HTTPException(400, detail="User already exists with that name.")

    user = User(**user_create.dict())
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.get("/{user_id}", status_code=200)
def get_user(user_id: int, db: Session = Depends(get_db)) -> schemas.User:
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(404, detail="User does not exist.")

    return user


@router.patch("/{user_id}", status_code=200)
def update_user(
    user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)
) -> schemas.User:
    user_query = db.query(User).filter_by(id=user_id)
    if not user_query.first():
        raise HTTPException(404, detail="User does not exist.")

    user_query.update(user_update.dict(), synchronize_session=False)

    user = user_query.first()
    db.commit()
    db.refresh(user)

    return user


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(404, detail="User does not exist.")

    db.delete(user)
    db.commit()

    return Response(status_code=204)
