from typing import Any, Dict
from fastapi import HTTPException, status
from src.modules.profiles.profile_models import Profile
from src.modules.profiles.profile_schemas import ProfileCreateRequest, ProfileDeleteRequest, ProfileGetRequest
from src.modules.profiles.profile_service import ProfileService

class ProfileController:

    def __init__(self, profile_service: ProfileService):
        self._profile_service = profile_service
    
    async def create_profile(self, request: ProfileCreateRequest, as_admin: bool = False):
        try:
            profile = Profile(
                org_id     = request.org_id,
                user_id    = request.user_id,
                first_name = request.first_name,
                last_name  = request.last_name,
                avatar_url = request.avatar_url,
                gender     = request.gender,
                email      = request.email,
                role       = request.role,
                status     = 'active'
            )
            return await self._profile_service.create_profile(profile, as_admin)
        except Exception as e:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))
    
    async def get_profile(self, request: ProfileGetRequest) -> Dict[str, Any]:
        try:
            profile_data = await self._profile_service.get_profile(request.user_id)
            return profile_data
        except Exception as e:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))

    async def delete_user(self, request: ProfileDeleteRequest):
        return await self._profile_service.delete_profile(request.profile_id, as_admin=True)
        