from src.modules.profiles.profile_models import Profile
from src.modules.profiles.profile_repository import ProfileRepository


class ProfileService:
    
    def __init__(self, profile_repository: ProfileRepository):
        self._profile_repository = profile_repository

    async def create_profile(self, profile: Profile, as_admin: bool = False):
        if as_admin:
            return await self._profile_repository.save_as_admin(profile.to_dict())
        return await self._profile_repository.save(profile.to_dict())
    
    async def delete_profile(self, profile_id: str, as_admin: bool = False):
        if as_admin:
            return await self._profile_repository.delete_as_admin(profile_id)
        return await self._profile_repository.delete(profile_id)
    



