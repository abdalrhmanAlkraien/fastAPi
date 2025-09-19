from typing import Any

from pydantic import BaseModel


class AuthorResponse(BaseModel):
    def __init__(self, author_id, name, age, /, **data: Any):
        super().__init__(**data)
        self.author_id = author_id
        self.name = name
        self.age = age
