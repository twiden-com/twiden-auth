from src.utils.datetime_utils import utc_now
from datetime import datetime, timezone
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
import uuid


# =====================================================
# REQUEST SCHEMAS (Input validation)
# =====================================================

class ProfileCreateRequest(BaseModel):
    user_id    : str
    email      : EmailStr
    first_name : Optional[str] = None
    last_name  : Optional[str] = None
    avatar_url : Optional[str] = None
    gender     : Optional[str] = None
    role       : str