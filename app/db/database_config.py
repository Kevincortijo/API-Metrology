from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

DATABASE_URL = ""

engine = create_engine(
    DATABASE_URL, echo=True, future=True, connect_args={"check_same_thread": False}
)

Sessionlocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def get_db():
    db: Session = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


class Base(DeclarativeBase):
    pass
