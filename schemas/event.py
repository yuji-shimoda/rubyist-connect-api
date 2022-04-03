from pydantic import BaseModel, Field, EmailStr, HttpUrl


class Event(BaseModel):
    id: int
    name: str
    created_at: date
    updated_at: date
    url: HttpUrl
