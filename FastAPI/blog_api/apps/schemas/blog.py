import datetime

from pydantic import BaseModel, Field


class BlogBase(BaseModel):
    title: str = Field(..., min_length=1, strip_whitespace=True)
    content: str = Field(..., min_length=1, strip_whitespace=True)


class BlogCreate(BlogBase):
    pass


class BlogUpdate(BlogBase):
    pass


class BlogResponse(BlogBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
