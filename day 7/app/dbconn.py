from .config import settings
import asyncpg

async def create_connection():
    pool = await asyncpg.create_pool(
        user = settings.db_user,
        password = settings.db_pwd,
        host = settings.db_host,
        port = settings.db_port,
        database = settings.db_name
    )

    return pool