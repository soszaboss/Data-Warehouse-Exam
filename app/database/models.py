from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# Classe de base sans colonne
class Base(DeclarativeBase):
    pass

# Modèle GDP
class GDP(Base):
    __tablename__ = "gdp"

    id: Mapped[int] = mapped_column(primary_key=True)
    country: Mapped[str] = mapped_column(String(150))
    country_code: Mapped[str] = mapped_column(String(3))
    year: Mapped[int] = mapped_column(Integer)
    inflation: Mapped[float] = mapped_column(Float)

# Modèle Consumer
class Consumer(Base):
    __tablename__ = "consumer"

    id: Mapped[int] = mapped_column(primary_key=True)
    country: Mapped[str] = mapped_column(String(150))
    country_code: Mapped[str] = mapped_column(String(3))
    year: Mapped[int] = mapped_column(Integer)
    inflation: Mapped[float] = mapped_column(Float)
