from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
from app.routers.companies import r
from contextlib import asynccontextmanager

app = FastAPI()
'''
class output(BaseModel):
    no : str
@app.get("/companies/{company}",response_model = output)
async def givenumbers(company:str):
    return {"no":"88"}

''' '''
@app.get("/companies")
async def company(limit:int =Query(default =10,le=60,ge=0)):
    return {"companyid": "hello"}
'''
'''
class requestvalidate(BaseModel):
    name : str
    age : int
app.include_router(r)
@app.post("/companies")
async def response(companydetails : requestvalidate):
    return companydetails

app.include_router(r)   
def get_title():
    return "Hello World"
@app.get("/companies")
async def companies(title : str = Depends(get_title)):
    return {"title": title}
    '''
'''
@app.get("/companies/{company}")
async def company(company:int):
    if company!=1:
        raise HTTPException(
            status_code = 404,
            detail = "company not found"
        )
    return {"company":company,"name":"zylen"}
    '''
@asynccontextmanager
async def life(app:FastAPI):
    print("Started life")
    yield
    print("Stopped life")
app = FastAPI(lifespan = life)