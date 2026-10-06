import json

from .config import settings
import asyncpg


async def init_connection(connection):
    await connection.set_type_codec(
        "jsonb",
        encoder=json.dumps,
        decoder=json.loads,
        schema="pg_catalog"
    )


async def create_pool():

    pool = await asyncpg.create_pool(
        host=settings.db_host,
        port=settings.db_port,
        database=settings.db_name,
        user=settings.db_user,
        password=settings.db_password,
        init=init_connection
    )

    return pool