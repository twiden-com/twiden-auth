

from src.modules.profiles.profile_schemas import ProfileCreateRequest


class ProfileService:
    
    def __init__(self, profile_repository):
        self._profile_repository = profile_repository

    def create_profile(self, profile: ProfileCreateRequest):
        pass


