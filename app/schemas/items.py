from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    name:str
    code:str
    quantity:int
    supplier:str
    unit_price:float
    descripition:str    

class ItemCreate(ItemBase):pass

class ItemRead(ItemBase):
    id:int

    class Config:
        orm_mode=True

class ItemUpdate(ItemBase):
    name:Optional[str] = None
    code:Optional[str] = None
    quantity:Optional[int] = None
    supplier:Optional[str] = None
    unit_price:Optional[float] = None
    descripition:Optional[str] = None    
