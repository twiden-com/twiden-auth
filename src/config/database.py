import asyncio
from supabase import acreate_client, AsyncClient
from supabase.lib.client_options import ClientOptions
from src.config.settings import settings

async def create_supabase() -> AsyncClient:
    supabase: AsyncClient = await acreate_client(
        settings.supabase_url, 
        settings.supabase_key,
        options=ClientOptions(
            auto_refresh_token=False,
            persist_session=False,
            storage=None,
            flow_type="implicit"
        )
    )
    return supabase

async def create_admin_supabase() -> AsyncClient:
    supabase: AsyncClient = await acreate_client(
        settings.supabase_url, 
        settings.supabase_service_key,
        options=ClientOptions(
            auto_refresh_token=False,
            persist_session=False,
            storage=None,
            flow_type="implicit"
        )
    )
    return supabase

# Global clients
_db_client: AsyncClient = None
_db_admin_client: AsyncClient = None
_client_lock = asyncio.Lock()

async def get_db_client() -> AsyncClient:
    global _db_client
    if _db_client is None:
        async with _client_lock:
            if _db_client is None:
                _db_client = await create_supabase()
    return _db_client

async def get_admin_db_client() -> AsyncClient:
    global _db_admin_client
    if _db_admin_client is None:
        async with _client_lock:
            if _db_admin_client is None:
                _db_admin_client = await create_admin_supabase()
    return _db_admin_client

async def close_db_connections():
    global _db_client, _db_admin_client
    
    if _db_client:
        await _db_client.auth.sign_out()
        _db_client = None
    
    if _db_admin_client:
        await _db_admin_client.auth.sign_out()
        _db_admin_client = None