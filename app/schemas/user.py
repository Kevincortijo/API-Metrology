from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name:str
    email:EmailStr
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
    email:Optional[EmailStr] = None
    sector:Optional[str] = None
    registration:Optional[str] = None
    rfid_code:Optional[str] = None    