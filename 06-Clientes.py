from common import table_registry
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func

from .common import table_registry

@table_registry.mapped_as_dataclass
class Product:
    __tablename__ = 'Clientes'

    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    description: Mapped[str] = mapped_column(nullable=False)
    value: Mapped[float] = mapped_column(nullable=False)
    points: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
