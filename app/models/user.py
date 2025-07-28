from app.db.database_config import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from sqlalchemy import ForeignKey

nome
setor
matricula
rfid

class User(Base):
    __tablename__='user'

    name:Mapped[str]
    sector:Mapped[str]
    registration:Mapped[str]
    rfid_code:Mapped[str]