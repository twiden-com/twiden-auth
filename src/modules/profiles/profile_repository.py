from src.config.database import Client

class ProfileRepository:
    
    def __init__(self, db_client: Client):
        self._db_client  = db_client
        self._table_name = 'profiles'
    
    async def save(self, profile):
        # self._db_client.table(self._table_name).insert(profile)
        pass
