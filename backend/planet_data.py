from typing import Sequence

from sqlmodel import Session, select

from backend.models import CelestialBody, Galaxy, StarSystem

ALL_PLANETS: list[tuple[str, float]] = [
    ("Mercury", 0.39),
    ("Venus", 0.72),
    ("Earth", 1.0),
    ("Mars", 1.52),
    ("Jupiter", 5.20),
    ("Saturn", 9.58),
    ("Uranus", 19.18),
    ("Neptune", 30.07),
]

ALL_STARS: list[tuple[str, float]] = [
    ("Sol", 0.0),  # Add more stars as needed
]

MILKY_WAY = Galaxy(
    name="Milky Way",
    position_x=0.0,
    position_y=0.0,
    position_z=0.0,
)

SOL = StarSystem(
    name="Sol",
    position_x=0.0,
    position_y=0.0,
    position_z=0.0,
    galaxy_id=None,  # Will be set dynamically
)


def insert_star_system(
    session: Session,
    planets: Sequence[str] | None = None,
    stars: Sequence[str] | None = None,
):
    # Check if the star system already exists
    statement = select(StarSystem).where(StarSystem.name == "Sol")
    result = session.exec(statement).first()
    if result:
        return

    milky_way = Galaxy(
        name=MILKY_WAY.name,
        position_x=MILKY_WAY.position_x,
        position_y=MILKY_WAY.position_y,
        position_z=MILKY_WAY.position_z,
    )
    session.add(milky_way)
    session.flush()

    sol = StarSystem(
        name=SOL.name,
        position_x=SOL.position_x,
        position_y=SOL.position_y,
        position_z=SOL.position_z,
        galaxy_id=milky_way.id,
    )
    session.add(sol)
    session.flush()

    planet_data = ALL_PLANETS
    if planets is not None:
        planet_data = [p for p in ALL_PLANETS if p[0] in planets]

    star_data = ALL_STARS
    if stars is not None:
        star_data = [s for s in ALL_STARS if s[0] in stars]

    body_objs = [
        CelestialBody(
            name=name,
            position_x=pos,
            position_y=0.0,
            position_z=0.0,
            type="planet",
            star_system_id=sol.id,
        )
        for name, pos in planet_data
    ] + [
        CelestialBody(
            name=name,
            position_x=pos,
            position_y=0.0,
            position_z=0.0,
            type="star",
            star_system_id=sol.id,
        )
        for name, pos in star_data
    ]
    session.add_all(body_objs)
    session.commit()
    return milky_way, sol, body_objs
