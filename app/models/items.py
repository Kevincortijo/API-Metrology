from app.db.database_config import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List, Optional


class Items(Base):
    __tablename__ = "item"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str]
    code: Mapped[str]
    quantity: Mapped[int]
    supplier: Mapped[str]
    unit_price: Mapped[float]
    descripition: Mapped[str]

    def __repr__(self) -> str:
        return f"Item(name={self.name},code={self.code},quantity={self.quantity},supplier={self.supplier},unit_price={self.unit_price},descripition={self.descripition})"
