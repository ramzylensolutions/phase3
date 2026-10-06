from fastapi import APIRouter,Depends,HTTPException
from ..dependencies.database import get_connection
from ..dependencies.auth import verify_token
from ..models.company import CompanyResponse
from uuid import UUID

router = APIRouter(prefix = "/companies",tags = ["companies"],
                   dependencies=[Depends(verify_token)]
)
@router.get("/{company_id}",response_model=CompanyResponse)
async def get_companies(company_id : UUID, connection = Depends(get_connection)):
    sql = "select id, name, domain, industry, employees, active, metadata, created_at from companies where id = $1"
    rows = await connection.fetchrow(sql,company_id)
    if rows is None:
        raise HTTPException(
            status_code=404,
            detail=f"Company with ID {company_id} was not found."
        )
    print (dict(rows).items())
    return dict(rows.items())