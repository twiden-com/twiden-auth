from src.config.database import AsyncClient

class ProfileRepository:
    pass
    
    def __init__(self, db_client: AsyncClient):
        self._db_client  = db_client
        self._table_name = 'profiles'
    
    # async def save(self, profile):
    #     # self._db_client.table(self._table_name).insert(profile)
    #     pass
