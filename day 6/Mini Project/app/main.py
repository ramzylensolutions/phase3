from fastapi import FastAPI
from contextlib import asynccontextmanager
from .db import create_pool
from .routers.companies import router
@asynccontextmanager
async def lifespan(app:FastAPI):
    print("The Pool connection created")
    app.state.pool = await create_pool()
    yield
    await app.state.pool.close()
    print("The pool connection stopped")
app = FastAPI(lifespan=lifespan)
app.include_router(router)
