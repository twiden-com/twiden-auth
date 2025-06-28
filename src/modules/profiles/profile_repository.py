from src.config.database import AsyncClient

class ProfileRepository:
    
    def __init__(self, db_client: AsyncClient, db_admin_client: AsyncClient):
        self._db_client  = db_client
        self._db_admin_client = db_admin_client
        self._table_name = 'profiles'
    
    async def save(self, profile_data: dict):
        response = await self._db_client.table(self._table_name).insert(profile_data).execute()
        return response
    
    async def save_as_admin(self, profile_data: dict):
        response = await self._db_admin_client.table(self._table_name).insert(profile_data).execute()
        return response.data[0]
    
    async def delete(self, profile_id: str):
        response = await self._db_client.table(self._table_name).delete().eq('id', profile_id).execute()
        return response
    
    async def delete_as_admin(self, profile_id: str):
        response = await self._db_admin_client.table(self._table_name).delete().eq('id', profile_id).execute()
        return response