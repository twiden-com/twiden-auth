# di_container.py
from supabase import AsyncClient
from typing import Optional
from src.config.database import get_db_client
from src.modules.users.user_controller import UserController
from src.modules.auth.auth_controller import AuthController

class DIContainer:
    def __init__(self):
        self._db_client: AsyncClient = get_db_client()
        self._user_controller: Optional[UserController] = None
        self._auth_controller: Optional[AuthController] = None

    def get_db_client(self) -> AsyncClient:
        return self._db_client
    
    def get_user_controller(self) -> UserController:
        if self._user_controller is None:
           self._user_controller = UserController()
        return self._user_controller
    
    def get_auth_controller(self) -> AuthController:
        if self._auth_controller is None:
           self._auth_controller = AuthController(self.get_user_controller())
        return self._auth_controller

# Global container
_container: Optional[DIContainer] = None

def get_container() -> DIContainer:
    global _container
    if _container is None:
        _container = DIContainer()
    return _container