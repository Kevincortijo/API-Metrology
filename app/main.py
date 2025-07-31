from fastapi import FastAPI

from app.api.user_routes import router as user_router
from app.db.database_config import Base, engine

app = FastAPI(title='API Metrologia')
Base.metadata.create_all(engine)

app.include_router(user_router)

