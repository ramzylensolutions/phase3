'''from pydantic import BaseModel,Field
class sample(BaseModel):
    name : str = Field(Description = "Name", max_length = 10)
    age : int = Field(ge=18,le=100)
    email : str | None = None
s = sample(name="Mrithyun",age = 73,email = "ram@gmail.com")
print(s.name) 
from decimal import Decimal
from datetime import datetime,date
from uuid import UUID
from pydantic import BaseModel,field_validator,model_validator

class sample(BaseModel):
    id : UUID
    amount : Decimal
    closed_date : date
    created_at : datetime
    username: str
    pwd : str
    con_pwd : str
    @model_validator(mode='after')
    def checkpwd(self):
        if self.pwd != self.con_pwd:
            raise ValueError("Pssword doesn't match")
        return self
    @field_validator("username")
    @classmethod
    def checkname(cls,value):
        if ' ' in value:
            raise ValueError("Name cannot contain spaces")
        return value
data = {'id': UUID('550e8400-e29b-41d4-a716-446655440000'), 'amount': Decimal('1500.50'), 'closed_date': datetime.date(2026, 9, 23), 'created_at': datetime.datetime(2026, 9, 23, 15, 30), 'username': 'RamMrithyun', 'pwd': '123', 'con_pwd': '123'}
s = sample.model_validata(data)
print(s.model_dump())'''

from pydantic import BaseModel,ConfigDict
class sample(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name:str
    age : int
s = sample(name="ram",age=22,salary =43234)