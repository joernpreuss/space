from datetime import datetime
from typing import Sequence

# from rich import print
from skyfield.api import load  # type: ignore  # skyfield stubs may be missing
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


# type: ignore[no-untyped-def, return, arg-type, assignment, call-overload, misc]
def get_planet_positions(
    planet_names: Sequence[str], date: datetime | None = None
) -> dict[str, tuple[float, float, float]]:
    """
    Returns a dict mapping planet names to (x, y, z) positions in AU for the given date (default: now).
    """
    planets = load("de421.bsp")  # type: ignore
    ts = load.timescale()  # type: ignore
    t = ts.now() if date is None else ts.utc(date)  # type: ignore
    sun = planets["sun"]  # type: ignore
    name_map = {
        "Mercury": "mercury",
        "Venus": "venus",
        "Earth": "earth",
        "Mars": "mars",
        "Jupiter": "jupiter barycenter",
        "Saturn": "saturn barycenter",
        "Uranus": "uranus barycenter",
        "Neptune": "neptune barycenter",
    }
    positions = {}
    for name in planet_names:
        key = name_map.get(name)
        if key is None:
            continue
        planet = planets[key]  # type: ignore
        pos = planet.at(t).observe(sun).apparent().position.au  # type: ignore
        positions[name] = (float(pos[0]), float(pos[1]), float(pos[2]))  # type: ignore
        # print(f"{name}: {positions[name]}")
    return positions  # type: ignore


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
    planet_names = [p[0] for p in planet_data]
    planet_positions = get_planet_positions(planet_names)

    star_data = ALL_STARS
    if stars is not None:
        star_data = [s for s in ALL_STARS if s[0] in stars]

    body_objs = [
        CelestialBody(
            name=name,
            position_x=planet_positions.get(name, (pos, 0.0, 0.0))[0],
            position_y=planet_positions.get(name, (pos, 0.0, 0.0))[1],
            position_z=planet_positions.get(name, (pos, 0.0, 0.0))[2],
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
