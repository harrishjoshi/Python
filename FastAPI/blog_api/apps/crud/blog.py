from apps.models.blog import Blog
from apps.schemas.blog import BlogCreate
from sqlalchemy.orm import Session


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
