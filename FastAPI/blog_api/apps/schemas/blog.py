from pydantic import BaseModel, field_validator


class PayloadValidation:
    @field_validator("title")
    @classmethod
    def title_not_empty(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError("title must not be empty")
        return v.strip()

    @field_validator("content")
    @classmethod
    def content_not_empty(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError("content must not be empty")
        return v.strip()


class BlogBase(BaseModel):
    title: str
    content: str


class BlogCreate(BlogBase, PayloadValidation):
    pass


class BlogUpdate(BlogBase, PayloadValidation):
    pass


class BlogResponse(BlogBase):
    id: int

    class Config:
        from_attributes = True
