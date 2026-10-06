from fastapi import FastAPI
from contextlib import asynccontextmanager
from .dbconn import create_connection
from .routers.maincompanies import router
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("The Application is started and the Pool is created!!")
    print()
    app.state.pool =await create_connection()
    yield
    app.state.pool.close()
    print("The Application is closed and the Pool is destroyed")
app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
