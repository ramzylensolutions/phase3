from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
class CompanyResponse(BaseModel):
    id : UUID
    name : str
    domain : str
    industry : str
    employees : int
    active : bool
    metadata : dict
    created_at : datetime