from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
class insertcompanies(BaseModel):
    id: UUID
    name: str
    domain: str
    industry: str
    employees : int
    active : bool
    metadata : dict
    created_at: datetime

class insertdomain(BaseModel):
    domain :str
    name : str
class insertone(BaseModel):
    oldname:str
    newname:str
