from pydantic import BaseModel, Field, EmailStr, HttpUrl, IPvAnyAddress
from typing import Optional, Literal, Union
from datetime import datetime, date


class UserSchema(BaseModel):
    id: int = Field(...)
    nickname: str = Field(...)
    github_id: int = Field(...)
    email: Union[str, None, Literal['']]
    introduction: Union[str, None, Literal['']]
    image: HttpUrl
    created_at: datetime
    updated_at: datetime
    twitter_name: Union[str, None, Literal['']]
    github_url: HttpUrl
    facebook_name: Union[str, None, Literal['']]
    location: Union[str, None, Literal['']]
    blog: Union[str, HttpUrl, None, Literal['']]
    sign_in_count: int = Field(...)
    current_sign_in_at: Union[datetime, None]
    last_sign_in_at: Union[datetime, None]
    current_sign_in_ip: Union[IPvAnyAddress, None]
    last_sign_in_ip: Union[IPvAnyAddress, None]
    qiita_name: Union[str, None, Literal['']]
    birthday: Union[date, None]
    profile_updated_at: Union[datetime, None]
    new_user_notification_enabled: bool = Field(...)
    first_active_at: Union[datetime, None]
