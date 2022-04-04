from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    image = Column(String)
    email = Column(String)
    introduction: Column(Text)
    created_at = Column(String)
    updated_at = Column(String)
    github_id = Column(String, unique=True, index=True)
    twitter_name = Column(String)
    github_url = Column(String)
    facebook_name = Column(String)
    nickname = Column(String, unique=True, index=True)
    location = Column(String)
    blog = Column(String)
    sign_in_count = Column(Integer)
    current_sign_in_at = Column(DateTime)
    last_sign_in_at = Column(DateTime)
    current_sign_in_ip = Column(String)
    last_sign_in_ip = Column(String)
    qiita_name = Column(String)
    birthday = Column(DateTime)
    profile_updated_at = Column(DateTime)
    new_user_notification_enabled = Column(Boolean)
    first_active_at = Column(DateTime)
