from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator
from typing import Dict, Optional, Any
from src.modules.auth.auth_enums import FlowType, LoginType
import uuid
import re

class SignUpRequest(BaseModel):
    first_name : str      = Field(None, min_length=1, max_length=50)
    last_name  : str      = Field(None, min_length=1, max_length=50)
    email      : EmailStr = Field(...)
    password   : str      = Field(... , min_length=8, max_length=50)
    username   : str      = Field(None, min_length=1, max_length=50)
    gender     : str      = Field(None, min_length=1, max_length=10)
    org_id     : str      = Field(... , min_length=5, max_length=50)
        
    model_config = ConfigDict(extra='forbid')


class SignUpResponse(BaseModel):
    message : str
    user    : Any
    profile : Any


class SignInRequest(BaseModel):
    email      : EmailStr = Field(...)
    password   : str      = Field(... , min_length=8, max_length=50)
    org_id     : str      = Field(... , min_length=5, max_length=50)

    model_config = ConfigDict(extra='forbid')

    @field_validator('org_id')
    @classmethod
    def validate_org_id(cls, v):
        try:
            uuid_obj = uuid.UUID(v)
            return str(uuid_obj)
        except ValueError:
            raise ValueError('org_id must be a valid UUID format')

class SignInResponse(BaseModel):
    user_id       : str = Field(... , min_length=5, max_length=50)
    org_id        : str = Field(... , min_length=5, max_length=50)
    access_token  : str = Field(...)
    refresh_token : str = Field(...)
    expires_at    : int = Field(...)
   

    model_config = ConfigDict(extra='forbid')

   
class GetSignedInUserRequest(BaseModel):
    access_token  : str = Field(...)

    model_config = ConfigDict(extra='forbid')


class GetSignedInUserResponse(BaseModel):
    user    : Dict[str, Any]  = Field(...)
    profile : Dict[str, Any]  = Field(...)
    
    model_config = ConfigDict(extra='forbid')