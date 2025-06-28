from pydantic import BaseModel, EmailStr, Field, HttpUrl, ConfigDict

# =====================================================
# REQUEST SCHEMAS (Input validation)
# =====================================================

class ProfileCreateRequest(BaseModel):
   model_config    = ConfigDict(extra='forbid')
   
   user_id    : str      = Field(... , min_length=1, max_length=100)
   org_id     : str      = Field(... , min_length=1, max_length=100)
   email      : EmailStr = Field(...)
   first_name : str      = Field(None, min_length=1, max_length=50)
   last_name  : str      = Field(None, min_length=1, max_length=50)
   avatar_url : HttpUrl  = Field(None, min_length=1, max_length=500)
   gender     : str      = Field(None, min_length=1, max_length=20)
   role       : str      = Field(... , min_length=1, max_length=100)

class ProfileGetRequest(BaseModel):
   model_config   = ConfigDict(extra='forbid')

   user_id    : str   = Field(..., min_length=1, max_length=100)

class ProfileDeleteRequest(BaseModel):
   model_config   = ConfigDict(extra='forbid')

   profile_id : str  = Field(..., min_length=1, max_length=50)