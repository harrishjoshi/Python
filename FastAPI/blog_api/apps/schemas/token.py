from pydantic import BaseModel


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int


class TokenData(BaseModel):
    user_id: int
    email: str
    token_type: str
    expires_at: int
    issued_at: int


class RefreshRequest(BaseModel):
    refresh_token: str
