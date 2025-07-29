from app.db.database_config import Base, engine
from app.service import user

from fastapi import FastAPI

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(user.router)