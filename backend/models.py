from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel  # type: ignore

if TYPE_CHECKING:
    from backend.models import Galaxy, StarSystem


class Planet(SQLModel, table=True):
    __tablename__ = "planet"  # type: ignore
    id: int | None = Field(default=None, primary_key=True)
    name: str
    position_x: float
    position_y: float
    position_z: float
    star_system_id: int | None = Field(default=None, foreign_key="starsystem.id")
    star_system: "StarSystem" = Relationship(back_populates="planets")


class StarSystem(SQLModel, table=True):
    __tablename__ = "starsystem"  # type: ignore
    id: int | None = Field(default=None, primary_key=True)
    name: str
    position_x: float
    position_y: float
    position_z: float
    galaxy_id: int | None = Field(default=None, foreign_key="galaxy.id")
    planets: list[Planet] = Relationship(back_populates="star_system")
    galaxy: "Galaxy" = Relationship(back_populates="star_systems")


class Galaxy(SQLModel, table=True):
    __tablename__ = "galaxy"  # type: ignore
    id: int | None = Field(default=None, primary_key=True)
    name: str
    position_x: float
    position_y: float
    position_z: float
    star_systems: list[StarSystem] = Relationship(back_populates="galaxy")
