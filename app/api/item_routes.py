from fastapi import APIRouter, Depends, HTTPException

from app.db.database_config import Session, get_db
from app.schemas.items import *
from app.service.items_service import *

router = APIRouter('/items', tags=['Item'])

@router.post('/register', response_model=ItemRead, status_code=200)
def register_new_item(item: ItemCreate, db:Session = Depends(get_db)):
    return create_item(db, item)

@router.get('/list_items', response_model=ItemRead, status_code=201)
def list_all_items(db:Session = Depends(get_db)):
    return get_all_items(db)

@router.get('/{item_id}', response_model=ItemRead, status_code=200)
def get_item(item_id: int, db:Session=Depends(get_db)):
    item = get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')
    
    return item

@router.put('/{item_item}', response_model=ItemRead, status_code=200)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    updated = update_item(db, item_id, item)
    if not updated:
        raise HTTPException(status_code=406,
                            detail='Item did not update')

@router.delete('/{item_id}', status_code=200)
def delete_item_info(item_id:int , db: Session = Depends(get_db)):
    deleted = delete_item(db, item_id)
    if not deleted:
        raise HTTPException(status_code=406,
                            detail='Item did not delete')