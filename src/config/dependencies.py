from fastapi import Depends
from src.config.container import get_container, DIContainer
from src.modules.profiles.profile_controller import ProfileController
from src.modules.auth.auth_controller  import AuthController
from src.modules.organizations.organization_controller import OrganizationController
from supabase import AsyncClient

__all__ = [
    "get_profile_controller", "ProfileController",
    "get_auth_controller", "AuthController",
    "get_org_controller", "OrganizationController"
]


async def get_profile_controller(container: DIContainer = Depends(get_container)) -> ProfileController:
    return await container.get_profile_controller()  

async def get_auth_controller(container: DIContainer = Depends(get_container)) -> AuthController:
    return await container.get_auth_controller()

async def get_org_controller(container: DIContainer = Depends(get_container)) -> OrganizationController:
    return await container.get_org_controller()