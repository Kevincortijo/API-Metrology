from typing import List, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database_config import Base


class User(Base):
    __tablename__ = 'user'
    id:Mapped[int] = mapped_column(primary_key=True, index=True)

    name:Mapped[str]
    sector:Mapped[str]
    registration:Mapped[str]
    rfid_code:Mapped[str]

    def __repr__(self) -> str:
        return (
            f'User(name={self.name}, '
            f'sector={self.sector}, '
            f'registration={self.registration}, '
            f'rfid_code={self.rfid_code}'
        )