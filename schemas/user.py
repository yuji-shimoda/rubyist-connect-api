from pydantic import BaseModel, Field, EmailStr, HttpUrl


class User(BaseModel):
    github_id: int = Field(...)
    name: str
    image: HttpUrl
    email: EmailStr
    nickname: str
    location: str
    github_url: HttpUrl
    blog: HttpUrl
