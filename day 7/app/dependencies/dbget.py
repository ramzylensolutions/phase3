from fastapi import Request
async def get_a_singlepool(request : Request):
    pool = request.app.state.pool
    async with pool.acquire() as connection:
        yield connection