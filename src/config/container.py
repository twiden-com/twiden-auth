from supabase import Client, AsyncClient
from typing import Optional
from src.config.database import get_db_client, get_admin_db_client
from src.modules.profiles.profile_controller import ProfileController
from src.modules.auth.auth_controller import AuthController

from src.modules.organizations.organization_controller import OrganizationController
from src.modules.organizations.organization_service  import OrganizationService
from src.modules.organizations.organization_repository import OrganizationRepository

from src.modules.profiles.profile_controller import ProfileController
from src.modules.profiles.profile_service import ProfileService
from src.modules.profiles.profile_repository import ProfileRepository

from src.modules.auth.auth_controller import AuthController
from src.modules.auth.auth_service import AuthService
from src.modules.auth.auth_repository import AuthRepository

class DIContainer:
    def __init__(self):
        self._db_client: AsyncClient = None
        self._db_admin_client: AsyncClient = None
        self._profile_controller : Optional[ProfileController] = None
        self._profile_service    : Optional[ProfileService] = None
        self._profile_repository : Optional[ProfileRepository] = None
        self._auth_controller    : Optional[AuthController] = None        
        self._auth_service       : Optional[AuthService] = None
        self._auth_repository    : Optional[AuthRepository] = None
        self._org_controller     : Optional[OrganizationController] = None
        self._org_service        : Optional[OrganizationService] = None
        self._org_repository     : Optional[OrganizationRepository] = None

    async def get_db_client(self) -> AsyncClient:  # Make it async again
        if self._db_client is None:
            self._db_client = await get_db_client()  # Now we need await
        return self._db_client
    
    async def get_db_admin_client(self) -> AsyncClient:
        if self._db_admin_client is None:
            self._db_admin_client = await get_admin_db_client()
        return self._db_admin_client
    
    # =====================================================
    # USER DI - (USER CRUD SERVICE)
    # =====================================================
    
    async def get_profile_controller(self) -> ProfileController:
        if self._profile_controller is None:
           self._profile_controller = ProfileController(await self.get_profile_service())
        return self._profile_controller
    
    async def get_profile_service(self) -> ProfileService:
        if self._profile_service is None:
            self._profile_service = ProfileService(await self.get_profile_repository())
        return self._profile_service
    
    async def get_profile_repository(self) -> ProfileRepository:
        if self._profile_repository is None:
            self._profile_repository = ProfileRepository(await self.get_db_client(), await self.get_db_admin_client())  # Add await back
        return self._profile_repository
    
    # =====================================================
    # AUTH DI - (ORCHESTRATION SERVICE)
    # =====================================================
    
    async def get_auth_controller(self) -> AuthController:
        if self._auth_controller is None:
           self._auth_controller = AuthController(
                await self.get_auth_service(), 
                await self.get_profile_controller(), 
                await self.get_org_controller()
               )
        return self._auth_controller
    
    async def get_auth_service(self) -> AuthService:
        if self._auth_service is None:
           self._auth_service = AuthService(await self.get_auth_repository())
        return self._auth_service
    
    async def get_auth_repository(self) -> AuthRepository:
        if self._auth_repository is None:
           self._auth_repository = AuthRepository(await self.get_db_client(), await self.get_db_admin_client())  # Add await back
        return self._auth_repository
    
    # =====================================================
    # ORGANIZATION DI - (ORG CRUD SERVICE)
    # =====================================================
    
    async def get_org_controller(self) -> OrganizationController:
        if self._org_controller is None:
           self._org_controller = OrganizationController(await self.get_org_service())
        return self._org_controller
    
    async def get_org_service(self) -> OrganizationService:
        if self._org_service is None:
            self._org_service = OrganizationService(await self.get_org_repository())
        return self._org_service
    
    async def get_org_repository(self) -> OrganizationRepository:
        if self._org_repository is None:
            self._org_repository = OrganizationRepository(await self.get_db_client())  # Add await back
        return self._org_repository
    

# Global container
_container: Optional[DIContainer] = None

def get_container() -> DIContainer:
    global _container
    if _container is None:
        _container = DIContainer()
    return _container