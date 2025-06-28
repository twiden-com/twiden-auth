import os
import asyncio
from supabase import acreate_client, AsyncClient

url = "https://zwbyjsdlpdwubkbriwea.supabase.co"
api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp3Ynlqc2RscGR3dWJrYnJpd2VhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA0NzIxMDEsImV4cCI6MjA2NjA0ODEwMX0.aLytDhKgdbDO60M8_xCtZVxUjCQJ1CQB_LAdqklib4c"
service_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp3Ynlqc2RscGR3dWJrYnJpd2VhIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MDQ3MjEwMSwiZXhwIjoyMDY2MDQ4MTAxfQ.Yb8f2-WJC5zpt7vIBII5fVXvcMvW_jaWu1ScY_AY46A"

async def create_supabase() -> AsyncClient:
    supabase: AsyncClient = await acreate_client(url, api_key)
    return supabase

async def create_admin_supabase() -> AsyncClient:
    supabase: AsyncClient = await acreate_client(url, service_key)
    return supabase

# Global client variable
_db_client: AsyncClient = None
_db_admin_client: AsyncClient = None

async def get_db_client() -> AsyncClient:
    global _db_client
    if _db_client is None:
        _db_client = await create_supabase()
    return _db_client

async def get_admin_db_client() -> AsyncClient:
    global _db_admin_client
    if _db_admin_client is None:
        _db_admin_client = await create_admin_supabase()
    return _db_admin_client