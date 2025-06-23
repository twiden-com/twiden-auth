from src.modules.auth.auth_repository import AuthRepository

class AuthService:

    def __init__(self, auth_repository: AuthRepository):
        self._auth_repository = auth_repository

    def sign_up(self, username: str, password: str):
        return self._auth_repository.signup(username, password)
