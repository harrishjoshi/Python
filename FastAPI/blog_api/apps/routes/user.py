from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from apps.crud import user
from apps.database import get_db
from apps.schemas.user import UserCreate, UserResponse, UserUpdate

router = APIRouter()


@router.post("/", response_model=UserResponse)
def create_user(request: UserCreate, db: Session = Depends(get_db)):
    db_user = user.get_by_email(db, request.email)
    if db_user:
        raise HTTPException(
            status_code=409,
            detail=f"A user with this email [{request.email}] already exists",
        )

    return user.create(db, request=request)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    return user.get(db, user_id)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, request: UserUpdate, db: Session = Depends(get_db)):
    db_user = user.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

    return user.update(db, db_obj=db_user, request=request)


@router.delete("/{user_id}", response_model=dict)
def delete(user_id: int, db: Session = Depends(get_db)):
    db_user = user.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

    user.delete(db, user_id)

    return {"message": "User deleted successfully"}


@router.get("/", response_model=list[UserResponse])
def get_all_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return user.get_multi(db, skip=skip, limit=limit)
