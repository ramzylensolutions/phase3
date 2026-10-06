from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal
class companies(BaseModel):
    name : str
    total_amount : Decimal
    total_deals : int
class name_check(BaseModel):
    name:str

