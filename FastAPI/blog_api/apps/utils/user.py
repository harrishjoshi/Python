from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from apps.constants.jwt import ALGORITHM, SECRET_KEY
from apps.crud import user
from apps.database import get_db
from apps.schemas.token import TokenData
from apps.utils.security import InvalidTokenError, Token


def get_token_data(token: str) -> TokenData:
    try:
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")

        if email is None:
            raise InvalidTokenError("Token missing subject claim")

        token_data = TokenData(
            user_id=payload.get("user_id"),
            email=email,
            token_type=payload.get("token_type", "access"),
            expires_at=payload.get("exp"),
            issued_at=payload.get("iat"),
        )

        # Validate token expiration
        if Token.is_token_expired(token_data):
            raise InvalidTokenError("Token has expired")

        return token_data

    except JWTError as e:
        raise InvalidTokenError(f"Invalid token: {str(e)}")


def verify_token(token: str, db: Session) -> TokenData:
    try:
        token_data = get_token_data(token)

        # Fetch the user from the database
        db_user = user.get_by_email(db=db, email=token_data.email)
        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return token_data
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token verification failed: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )
