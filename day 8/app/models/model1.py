from pydantic import BaseModel
class sendingmodel(BaseModel):
    name : str
    age : int
class receivingmodel(BaseModel):
    id : int
class insertone(BaseModel):
    oldname:str
    newname:str 

class insert_a_row(BaseModel):
    name: str
    domain: str
    industry : str
    employees: int
    active: bool
    metadata: dict