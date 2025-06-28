from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Dict, Optional, Any
from src.modules.auth.auth_enums import FlowType, LoginType


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

class SignInResponse(BaseModel):
    user_id       : str = Field(... , min_length=5, max_length=50)
    org_id        : str = Field(... , min_length=5, max_length=50)
    access_token  : str = Field(...)
    refresh_token : str = Field(...)
    expires_at    : int = Field(...)
   

    model_config = ConfigDict(extra='forbid')

   
