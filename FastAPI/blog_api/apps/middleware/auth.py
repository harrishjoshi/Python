from fastapi import Request, status
from fastapi.responses import JSONResponse

from apps.crud import user
from apps.database import SessionLocal
from apps.utils import user as userUtils


async def auth_middleware(request: Request, call_next):
    # Exclude public endpoints
    public_paths = ["/login", "/", "/docs", "/redoc", "/openapi.json"]
    if request.url.path in public_paths:
        response = await call_next(request)
        return response

    # Check for Authorization header
    authorization = request.headers.get("Authorization")
    if not authorization or not authorization.startswith("Bearer "):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Invalid authentication header. Use 'Bearer <token>'"},
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create a database session
    db = SessionLocal()
    try:
        # Extract token
        token = authorization.split("Bearer ")[1]

        # Get token data without database validation first
        token_data = userUtils.get_token_data(token)

        # Verify user exists in database
        db_user = user.get_by_email(db=db, email=token_data.email)
        if not db_user:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "User not found"},
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Store user details in request state
        request.state.user_id = token_data.user_id
        request.state.user_email = token_data.email

        # Process the request
        response = await call_next(request)
        return response

    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": str(e)},
            headers={"WWW-Authenticate": "Bearer"},
        )
    finally:
        # Close the database session
        db.close()
