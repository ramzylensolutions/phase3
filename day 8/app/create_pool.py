import asyncpg
from .envretrive import settings
async def create_pool_connection():
    pool = await asyncpg.create_pool(
        user = settings.db_user,
        password = settings.db_passwrod,
        host = settings.db_host,
        port = settings.db_port,
        database= settings.db_name
    )
    return pool