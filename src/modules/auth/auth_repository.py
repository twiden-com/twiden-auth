# from src.config.database import Client
from supabase import AsyncClient


class AuthRepository:
    
    def __init__(self, db_client: AsyncClient):
        self._db_client = db_client

    async def signup(self, email: str, password: str):
        response =  await self._db_client.auth.sign_up({'email': email, 'password': password})
        return response