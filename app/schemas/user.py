from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    name: str
    sector: str
    registration:str
    rfid_code:str

    class Config:
        orm_mode: True

class UserCreate(BaseModel):
    name:str
    sector:str
    registration:str
    rfid_code:str