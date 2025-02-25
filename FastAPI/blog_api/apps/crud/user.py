from sqlalchemy.orm import Session

from apps.models.user import User
from apps.schemas.user import UserCreate, UserUpdate


def create(db: Session, request: UserCreate):
    user = User(**request.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_by_email(db: Session, email):
    return db.query(User).filter(User.email == email).first()


def get(db: Session, id):
    return db.query(User).filter(User.id == id).first()


def get_multi(db: Session, skip: int, limit: int):
    return db.query(User).offset(skip).limit(limit).all()


def update(db: Session, db_obj: User, request: UserUpdate):
    update_data = request.dict(exclude_unset=True)  # Only update provided fields
    for key, value in update_data.items():
        setattr(db_obj, key, value)

    db.commit()
    db.refresh(db_obj)

    return db_obj


def delete(db: Session, id: int):
    db_obj = db.query(User).filter(User.id == id).first()
    if db_obj:
        db.delete(db_obj)
        db.commit()

    return None
