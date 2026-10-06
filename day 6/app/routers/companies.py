from fastapi import FastAPI,APIRouter,Depends
def access_check():
    return "Access Granted"
r = APIRouter(prefix = "/companies",dependencies = [Depends(access_check)])
@r.get("/")
async def company():
    return "The Router Created"