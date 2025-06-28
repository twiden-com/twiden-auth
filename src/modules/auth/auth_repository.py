# from src.config.database import Client
from supabase import AsyncClient


class AuthRepository:
    
    def __init__(self, db_client: AsyncClient, db_admin_client: AsyncClient):
        self._db_client = db_client
        self._db_admin_client = db_admin_client

    async def signup(self, email: str, password: str):
        response =  await self._db_client.auth.sign_up({'email': email, 'password': password})
        return response.user
    
    async def signin(self, email: str, password: str):
        response =  await self._db_client.auth.sign_in_with_password({'email': email, 'password': password})
        return response
    
    async def delete_user(self, user_id: str):
        return await self._db_admin_client.auth.admin.delete_user(user_id)
    
    async def get_signed_in_user(self, access_token: str):
        return await self._db_client.auth.get_user(access_token)