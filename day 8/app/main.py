from fastapi import FastAPI
from .create_pool import create_pool_connection
from .routers.getcompany import router
async def lifespan(app:FastAPI):
    print("Pool Created Successfully")
    app.state.pool = await create_pool_connection()
    yield
    app.state.pool.close()
    print("Pool Closed Successfully")
app = FastAPI(lifespan=lifespan)
app.include_router(router)