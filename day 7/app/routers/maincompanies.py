from fastapi import APIRouter,Depends
from ..dependencies.auth import verify_token
from ..models.companies import name_check
from ..dependencies.dbget import get_a_singlepool
from fastapi import HTTPException
from ..models.insertcompanies import insertcompanies,insertdomain,insertone
from ..models.deletecompany import delete_company
from uuid import UUID

router = APIRouter(tags=["companies"])
@router.get('/company/{company_id}')
async def samplefun(company_id:UUID,connection = Depends(get_a_singlepool)):
    sql = """select name as Name from companies where id = $1"""
    rows = await connection.fetch(sql,company_id)
    return rows





























'''
@router.patch("/")
async def update_company(rows:insertone,connection = Depends(get_a_singlepool)):
    sql = """update companies
             set name = $1
             where name =$2"""
    await connection.execute(sql,rows.newname,rows.oldname)
    return "Updation Successfully Finished"
''''''
router = APIRouter(tags=["companies"], dependencies=[Depends(verify_token)])
@router.get("/{company_name}")
async def profit_check(company_name:str,connection=Depends(get_a_singlepool)):
    sql1="""select sum(s.amount)as Total_Income 
            from companies as c
            inner join sales as s
            on c.id = s.company_id
            where c.name = $1
            group by c.name;"""
    sql2="""select sum(e.amount) as Total_Expenses
            from companies as c
            inner join expenses as e
            on c.id = e.company_id 
            where name = $1
            group by c.name; """
    sql3="""select sum(d.deal_amount ) as deal_income ,sum(d.deal_expense ) as deal_expense
            from companies as c
            inner join deals as d
            on c.id = d.company_id 
            where c.name = $1 and d.status = 'won'
            group by c.name,d.status ;"""
    income = await connection.fetchval(sql1,company_name)
    expense = await connection.fetchval(sql2,company_name)
    dealincome = await connection.fetchrow(sql3,company_name)
    Profit = (income+(dealincome['deal_income']-dealincome['deal_expense'])) - expense 
    return f"The Total Profit of Profit {company_name} is rs.{Profit}"

@router.get("/summary",response_model=list[companies])
async def get_companies(connection = Depends(get_a_singlepool)):
    sql = "select c.name,sum(amount) as total_amount,count(*) as total_deals from companies as c inner join deals as d on c.id = d.company_id group by c.name"
    rows = await connection.fetch(sql)
    if rows is None:
        raise HTTPException(
            status_code=404,
            detail="Companies not found"
        )
    return [dict(row.items()) for row in rows]
@router.post("/")
async def insert_companies(rows : insertcompanies,connection = Depends(get_a_singlepool)):
    sql = "insert into companies(id,name,domain,industry,employees,active,metadata,created_at)values($1,$2,$3,$4,$5,$6,$7,$8)"
    await connection.execute(sql,rows.id,rows.name,rows.domain,rows.industry,rows.employees,rows.active,json.dumps(rows.metadata),rows.created_at)
    return "Company inserted successfully"

@router.patch("/")
async def update_companies(rows:insertdomain, connection = Depends(get_a_singlepool)):
    sql = """update companies set domain = $1 where name = $2"""
    await connection.execute(sql,rows.domain,rows.name)
    return "updation successful"
@router.delete("/")
async def delete_companies(name:str, connection = Depends(get_a_singlepool)):
    sql = """delete from companies where name = $1"""
    await connection.execute(sql,name)
    return "Deleted the row successfully"
'''