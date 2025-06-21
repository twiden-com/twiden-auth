from fastapi import Depends
from src.config.container import get_container, DIContainer
from src.modules.users.user_controller import UserController
from src.modules.auth.auth_controller  import AuthController


__all__ = [
    "get_user_controller", "UserController",
    "get_auth_controller", "AuthController"
]

def get_user_controller(container: DIContainer = Depends(get_container)) -> UserController:
    return container.get_user_controller()

def get_auth_controller(container: DIContainer = Depends(get_container)) -> AuthController:
    return container.get_auth_controller()