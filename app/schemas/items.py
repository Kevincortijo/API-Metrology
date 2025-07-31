from pydantic import BaseModel


class ItemCreate(BaseModel):
    name:str
    code:str
    quantity:int
    supplier:str
    unit_price:float
    descripition:str