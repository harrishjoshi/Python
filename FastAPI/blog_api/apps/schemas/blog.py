from pydantic import BaseModel, field_validator


class BlogBase(BaseModel):
    title: str
    content: str


class BlogCreate(BlogBase):
    pass


class BlogUpdate(BlogBase):
    pass


class BlogResponse(BlogBase):
    id: int

    class Config:
        from_attributes = True
