from pydantic import BaseModel, field_validator, ValidationError, EmailStr, Field
from typing import Dict, Optional, Any
from src.modules.auth.auth_enums import FlowType, LoginType


class SignUpRequest(BaseModel):
    first_name : Optional[str]  = None
    last_name  : Optional[str]  = None
    email      : EmailStr
    password   : str
    username   : str = None
    gender     : Optional[str]  = None
    meta_data  : 'MetaData'


class MetaData(BaseModel):
    flow: FlowType
    org_id: str = ""
    login_type: LoginType
    
    # @field_validator('flow')
    # @classmethod
    # def validate_flow(cls, v):
    #     # Only validate specific enum values if needed
    #     if v not in [FlowType.C2B, FlowType.B2B]:
    #         raise ValueError(f"Flow must be either {FlowType.C2B.value} or {FlowType.B2B.value}")
    #     return v
        







    