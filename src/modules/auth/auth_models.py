from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from datetime import datetime

@dataclass
class Identity:
    id: str
    user_id: str
    identity_data: Dict[str, Any]
    provider: str
    created_at: datetime
    last_sign_in_at: datetime
    updated_at: datetime

@dataclass
class AppMetadata:
    provider: str
    providers: List[str]

@dataclass
class User:
    id: str
    app_metadata: AppMetadata
    user_metadata: Dict[str, Any]
    aud: str
    confirmation_sent_at: Optional[datetime]
    recovery_sent_at: Optional[datetime]
    email_change_sent_at: Optional[datetime]
    new_email: Optional[str]
    invited_at: Optional[datetime]
    action_link: Optional[str]
    email: str
    phone: str
    created_at: datetime
    confirmed_at: Optional[datetime]
    email_confirmed_at: Optional[datetime]
    phone_confirmed_at: Optional[datetime]
    last_sign_in_at: Optional[datetime]
    role: str
    updated_at: datetime
    identities: List[Identity]
    factors: Optional[Any]

@dataclass
class SessionUser:
    # Same fields as User - you can inherit or duplicate
    id: str
    app_metadata: AppMetadata
    user_metadata: Dict[str, Any]
    aud: str
    confirmation_sent_at: Optional[datetime]
    recovery_sent_at: Optional[datetime]
    email_change_sent_at: Optional[datetime]
    new_email: Optional[str]
    invited_at: Optional[datetime]
    action_link: Optional[str]
    email: str
    phone: str
    created_at: datetime
    confirmed_at: Optional[datetime]
    email_confirmed_at: Optional[datetime]
    phone_confirmed_at: Optional[datetime]
    last_sign_in_at: Optional[datetime]
    role: str
    updated_at: datetime
    identities: List[Identity]
    factors: Optional[Any]

@dataclass
class Session:
    provider_token: Optional[str]
    provider_refresh_token: Optional[str]
    access_token: str
    refresh_token: str
    expires_in: int
    expires_at: int
    token_type: str
    user: SessionUser

@dataclass
class AuthResponse:
    user: User
    session: Session