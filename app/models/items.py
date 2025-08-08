from typing import List, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database_config import Base


class Item(Base):
    __tablename__ = "item"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str]
    code: Mapped[str]
    quantity: Mapped[int]
    supplier: Mapped[str]
    manufacturer: Mapped[str]
    unit_price: Mapped[float]
    descripition: Mapped[str]

    def __repr__(self) -> str:
        return (
            f'Item(name={self.name}, '
            f'code={self.code}, '
            f'quantity={self.quantity}, '
            f'supplier={self.supplier}, '
            f'unit_price={self.unit_price}, '
            f'descripition={self.descripition}'
        )
