from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Optional
import uuid


@dataclass
class Profile:
    user_id: uuid.UUID
    org_id: uuid.UUID
    email: str
    role: str 
    status: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    avatar_url: Optional[str] = None
    gender: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    def __post_init__(self):
        """Ensure timezone-aware datetimes after initialization"""
        if self.created_at is None:
            from src.utils.datetime_utils import utc_now
            self.created_at = utc_now()
        elif isinstance(self.created_at, datetime) and self.created_at.tzinfo is None:
            self.created_at = self.created_at.replace(tzinfo=timezone.utc)
            
        if self.updated_at is None:
            from src.utils.datetime_utils import utc_now
            self.updated_at = utc_now()
        elif isinstance(self.updated_at, datetime) and self.updated_at.tzinfo is None:
            self.updated_at = self.updated_at.replace(tzinfo=timezone.utc)
    
    def get_full_name(self) -> str:
        """Return full name or email if names are not available"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return self.email
    
    def is_active(self) -> bool:
        return self.status.lower() == "active"
    
    def is_admin(self) -> bool:
        return self.role.lower() == "admin"
    
    def update_timestamp(self):
        from src.utils.datetime_utils import utc_now
        self.updated_at = utc_now()
    
    def to_dict(self) -> dict:
        data = asdict(self)
    
        data['user_id'] = str(data['user_id'])
        data['org_id']  = str(data['org_id'])
        
        # Convert datetime to ISO string
        if data['created_at']:
            data['created_at'] = data['created_at'].isoformat()
        if data['updated_at']:
            data['updated_at'] = data['updated_at'].isoformat()
        return data
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Profile':
        return cls(**data)