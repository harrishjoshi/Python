from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from apps.crud import blog
from apps.database import get_db
from apps.schemas.blog import BlogCreate, BlogResponse, BlogUpdate

router = APIRouter()


@router.post("/", response_model=BlogResponse)
def create_blog(request: BlogCreate, db: Session = Depends(get_db)):
    return blog.create(db, request=request)


@router.get("/{blog_id}", response_model=BlogResponse)
def read_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = blog.get(db, id=blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail=f"Blog with id {blog_id} not found")

    return db_blog


@router.get("/", response_model=list[BlogResponse])
def read_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return blog.get_multi(db, skip=skip, limit=limit)


@router.put("/{blog_id}", response_model=BlogResponse)
def update_blog(blog_id: int, request: BlogUpdate, db: Session = Depends(get_db)):
    db_blog = blog.get(db, blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail=f"Blog with id {blog_id} not found")

    updated_blog = blog.update(db, db_obj=db_blog, request=request)

    return updated_blog


@router.delete("/{blog_id}", response_model=dict)
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = blog.get(db, blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail=f"Blog with id {blog_id} not found")

    blog.delete(db, id=blog_id)

    return {"message": "Blog deleted successfully"}
