from pydantic import BaseModel, Field


class AuthorRequest(BaseModel):
    name: str = Field(..., description="author should not be empty", min_length=1, max_length=100)
    age: int = Field(..., description="author age should not be empty", ge=18)