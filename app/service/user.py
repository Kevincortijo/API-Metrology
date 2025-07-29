from app.db.database_config import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse

from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends

router = FastAPI()


@router.post('/users/',response_model=UserResponse)
def create_user(user: UserCreate, db:Session=Depends(get_db)):
    db_user = User(name = user.name, 
                   sector = user.sector, 
                   registration = user.registration, 
                   rfid_code = user.rfid_code)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user