from pydantic import BaseModel



class UserMembershipRequest(BaseModel):
    org_id: str
    user_email: str