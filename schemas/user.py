from pydantic import BaseModel, Field, EmailStr, HttpUrl


class User(BaseModel):
    id: int = Field(...)
    name: str
    image: HttpUrl
    email: EmailStr
    introduction: str
    created_at: date
    updated_at: date
    github_id: int = Field(...)
    twitter_name: str
    github_url: HttpUrl
    facebook_name: str
    nickname: str
    location: str
    blog: HttpUrl
    sign_in_count: int
    current_sign_in_at: date
    last_sign_in_at: date
    current_sign_in_ip: str
    last_sign_in_ip: str
    qiita_name: str
    birthday: date
    profile_updated_at: date
    new_user_notification_enabled: bool
    first_active_at: date
