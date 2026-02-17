from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(..., min_length=3)
    username: str = Field(..., min_length=5)
    password: str = Field(..., min_length=8)
