from src.modules.profiles.profile_models import Profile
from src.modules.profiles.profile_schemas import ProfileCreateRequest
from src.modules.profiles.profile_service import ProfileService

class ProfileController:

    def __init__(self, profile_service):
        self._profile_service = profile_service
    
    # def create_profile(self, request: ProfileCreateRequest):
    #     pass
        