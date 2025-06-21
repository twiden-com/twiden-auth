from src.utils.datetime_utils import utc_now
from datetime import datetime, timezone
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
import uuid


class DBProfileCreate(BaseModel):
    user_id: uuid.UUID
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    avatar_url: Optional[str] = None
    gender: Optional[str] = None
    role: str = "user"
    status: str = "active"
    created_at: Optional[datetime] = Field(default_factory=utc_now)
    updated_at: Optional[datetime] = Field(default_factory=utc_now)
    
    @field_validator('created_at', 'updated_at', mode='before')
    @classmethod
    def ensure_timezone_aware(cls, v):
        if v is None:
            return utc_now()
        if isinstance(v, datetime) and v.tzinfo is None:
            return v.replace(tzinfo=timezone.utc)
        return v