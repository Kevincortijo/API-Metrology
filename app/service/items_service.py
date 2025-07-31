from sqlalchemy.orm import Session

from app.models.items import Item
from app.schemas.items import ItemCreate, ItemUpdate


def create_item(db:Session, item_data: ItemCreate):
    item = Item(**item_data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_all_items(db:Session):
    return db.query(Item).all()

def get_item(db:Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def update_item(db:Session, item_id:int, item_data:ItemUpdate):
    item = get_item(db,item_id)
    if item:
        for fields, value in item_data.model_dump(exclude_unset=True).items():
            setattr(item, fields, value)
        db.commit()
        db.refresh()
        return item

def delete_item(db: Session, item_id: int):
    item = get_item(db, item_id)
    if item:
        db.delete(item)
        db.commit()
    return item