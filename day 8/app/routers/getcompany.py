from fastapi import APIRouter,Depends
from ..dependencies.auth import verify_token
from ..models.model1 import insert_a_row
from ..dependencies.getapool import get_a_pool
NameCompany = None
NameTitle = None
router = APIRouter(tags=["companies"],dependencies=[Depends(verify_token)])
@router.get("/company/{company_id}")
async def getcompanyname(company_id ,connection = Depends(get_a_pool)):
    sql = """ select name as Name from companies where id = $1"""
    NameCompany  = await connection.fetchval(sql,company_id)
    return NameCompany
@router.get("deals/{title}")
async def getcompanyname(title ,connection = Depends(get_a_pool)):
    sql = """ select status as Name from deals where title = $1"""
    NameTitle  = await connection.fetchval(sql,title) 
    return NameTitle
@router.get("/givename")
async def getcompanyname():
    return {
        "company_name": NameCompany,
        "deal_name": NameTitle
    }  




















