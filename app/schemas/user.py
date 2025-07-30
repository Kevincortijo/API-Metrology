from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name:str
    sector:str
    registration:str
    rfid_code:str

class UserCreate(UserBase): pass

class UserRead(UserBase):
    id: int

    class Config:
        orm_mode: True

class UserUpdate(UserBase):
    name:Optional[str] = None
    sector:Optional[str] = None
    registration:Optional[str] = None
    rfid_code:Optional[str] = None    