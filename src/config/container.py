from supabase import Client
from typing import Optional
from src.config.database import get_db_client
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
        self._db_client: Client = get_db_client()
        self._profile_controller : Optional[ProfileController] = None
        self._profile_service    : Optional[ProfileService] = None
        self._profile_repository : Optional[ProfileRepository] = None
        self._auth_controller    : Optional[AuthController] = None        
        self._auth_service       : Optional[AuthService] = None
        self._auth_repository    : Optional[AuthRepository] = None
        self._org_controller     : Optional[OrganizationController] = None
        self._org_service        : Optional[OrganizationService] = None
        self._org_repository     : Optional[OrganizationRepository] = None

    def get_db_client(self) -> Client:
        return self._db_client
    
    # =====================================================
    # USER DI - (USER CRUD SERVICE)
    # =====================================================
    
    def get_profile_controller(self) -> ProfileController:
        if self._profile_controller is None:
           self._profile_controller = ProfileController(self.get_profile_service())
        return self._profile_controller
    
    def get_profile_service(self) -> ProfileService:
        if self._profile_service is None:
            self._profile_service = ProfileService(self.get_profile_repository())
        return self._profile_service
    
    def get_profile_repository(self) -> ProfileRepository:
        if self._profile_repository is None:
            self._profile_repository = ProfileRepository(self.get_db_client())
        return self._profile_repository
    
    # =====================================================
    # AUTH DI - (ORCHESTRATION SERVICE)
    # =====================================================
    
    def get_auth_controller(self) -> AuthController:
        if self._auth_controller is None:
           self._auth_controller = AuthController(
                self.get_auth_service(), 
                self.get_profile_controller(), 
                self.get_org_controller()
               )
        return self._auth_controller
    
    def get_auth_service(self) -> AuthService:
        if self._auth_service is None:
           self._auth_service = AuthService(self.get_auth_repository())
        return self._auth_service
    
    def get_auth_repository(self) -> AuthRepository:
        if self._auth_repository is None:
           self._auth_repository = AuthRepository(self.get_db_client())
        return self._auth_repository
    
    # =====================================================
    # ORGANIZATION DI - (ORG CRUD SERVICE)
    # =====================================================
    
    def get_org_controller(self) -> OrganizationController:
        if self._org_controller is None:
           self._org_controller = OrganizationController(self.get_org_service())
        return self._org_controller
    
    def get_org_service(self) -> OrganizationService:
        if self._org_service is None:
            self._org_service = OrganizationService(self.get_org_repository())
        return self._org_service
    
    def get_org_repository(self) -> OrganizationRepository:
        if self._org_repository is None:
            self._org_repository = OrganizationRepository(self.get_db_client())
        return self._org_repository
    

# Global container
_container: Optional[DIContainer] = None

def get_container() -> DIContainer:
    global _container
    if _container is None:
        _container = DIContainer()
    return _container