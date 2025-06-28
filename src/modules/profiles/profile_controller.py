from src.modules.profiles.profile_models import Profile
from src.modules.profiles.profile_schemas import ProfileCreateRequest, ProfileDeleteRequest
from src.modules.profiles.profile_service import ProfileService

class ProfileController:

    def __init__(self, profile_service: ProfileService):
        self._profile_service = profile_service
    
    async def create_profile(self, request: ProfileCreateRequest, as_admin: bool = False):
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

    async def delete_user(self, request: ProfileDeleteRequest):
        return await self._profile_service.delete_profile(request.profile_id, as_admin=True)
        