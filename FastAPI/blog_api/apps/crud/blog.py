from sqlalchemy.orm import Session

from apps.models.blog import Blog
from apps.schemas.blog import BlogCreate, BlogUpdate


def create(db: Session, request: BlogCreate):
    blog = Blog(**request.model_dump())
    db.add(blog)
    db.commit()
    db.refresh(blog)

    return blog


def get(db: Session, id: int):
    return db.query(Blog).filter(Blog.id == id).first()


def get_multi(db: Session, skip: int, limit: int):
    return db.query(Blog).offset(skip).limit(limit).all()


def update(db: Session, db_obj: Blog, request: BlogUpdate):
    update_data = request.dict(exclude_unset=True)  # Only update provided fields
    for key, value in update_data.items():
        setattr(db_obj, key, value)

    db.commit()
    db.refresh(db_obj)

    return db_obj


def delete(db: Session, id: int):
    db_obj = db.query(Blog).filter(Blog.id == id).first()
    if db_obj:
        db.delete(db_obj)
        db.commit()

    return None
