from src.modules.auth.auth_repository import AuthRepository

class AuthService:

    def __init__(self, auth_repository: AuthRepository):
        self._auth_repository = auth_repository

    async def sign_up(self, email: str, password: str):
        return await self._auth_repository.signup(email, password)

    async def sign_in(self, email: str, password: str):
        return await self._auth_repository.signin(email, password)
    
    async def delete_user(self, user_id: str):
        return await self._auth_repository.delete_user(user_id)
    
    async def get_signed_in_user(self, access_token: str):
        return await self._auth_repository.get_signed_in_user(access_token)