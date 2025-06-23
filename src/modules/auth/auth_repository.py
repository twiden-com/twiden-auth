# from src.config.database import Client
from supabase import Client


class AuthRepository:
    
    def __init__(self, db_client: Client):
        self._db_client = db_client

    def signup(self, email: str, password: str):
        response =  self._db_client.auth.sign_up({'email': email, 'password': password})
        self._db_client.auth.
        return response.user