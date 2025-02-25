from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from apps.database import get_db
from apps.models.user import User
from apps.schemas.token import RefreshRequest, TokenResponse
from apps.utils.security import Hash, InvalidTokenError, Token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=TokenResponse)
def login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    # Find the user by email
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Verify the password
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create token data
    token_data = {"sub": user.email, "user_id": user.id}

    # Generate access and refresh tokens
    access_token = Token.create_access_token(data=token_data)
    refresh_token = Token.create_refresh_token(data=token_data)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "expires_in": 30 * 60,  # 30 minutes in seconds
    }


@router.post("/refresh", response_model=TokenResponse)
def refresh_token(
    refresh_request: RefreshRequest = Body(...), db: Session = Depends(get_db)
):
    try:
        # Verify the refresh token
        token_data = Token.verify_token(refresh_request.refresh_token)

        # Check if it's actually a refresh token
        if getattr(token_data, "token_type", None) != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Check if token is expired
        if Token.is_token_expired(token_data):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Get the user
        user = db.query(User).filter(User.email == token_data.email).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Create new token data
        new_token_data = {"sub": user.email, "user_id": user.id}

        # Generate new access and refresh tokens
        access_token = Token.create_access_token(data=new_token_data)
        refresh_token = Token.create_refresh_token(data=new_token_data)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "expires_in": 30 * 60,  # 30 minutes in seconds
        }

    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
