import os
import asyncio
from supabase import acreate_client, AsyncClient

url = "https://zwbyjsdlpdwubkbriwea.supabase.co"
api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp3Ynlqc2RscGR3dWJrYnJpd2VhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA0NzIxMDEsImV4cCI6MjA2NjA0ODEwMX0.aLytDhKgdbDO60M8_xCtZVxUjCQJ1CQB_LAdqklib4c"

async def create_supabase() -> AsyncClient:
    supabase: AsyncClient = await acreate_client(url, api_key)
    return supabase

# Global client variable
_db_client: AsyncClient = None

async def get_db_client() -> AsyncClient:
    global _db_client
    if _db_client is None:
        _db_client = await create_supabase()
    return _db_client