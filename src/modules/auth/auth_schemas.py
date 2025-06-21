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

    @field_validator('flow')
    @classmethod
    def is_valid_flow(cls, v):
        flow = v.get('flow')
        if flow and flow not in [FlowType.C2B, FlowType.B2B]:
            raise ValueError(f"Flow must be one of {[e.value for e in FlowType]}")
        return v
    
    @field_validator('login_type')
    @classmethod
    def is_valid_login_type(cls, v):
        login_type = v.get('login_type')
        allowed_types = [e.value for e in LoginType]
        if login_type and login_type not in allowed_types:
            raise ValueError(f"Login Type must be one of {allowed_types}")
        







    