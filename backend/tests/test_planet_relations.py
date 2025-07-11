from sqlmodel import Session, select

from backend.models import CelestialBody, Galaxy, StarSystem


def test_planet_star_system_relation(
    session: Session, test_data: tuple[Galaxy, StarSystem, list[CelestialBody]]
):
    _, star_system, _ = test_data
    statement = select(CelestialBody).where(
        CelestialBody.star_system_id == star_system.id, CelestialBody.type == "planet"
    )
    result = session.exec(statement).all()
    planet_names = {cb.name for cb in result}
    assert "Earth" in planet_names
    assert "Mars" in planet_names
    assert len(result) == 2


def test_star_system_galaxy_relation(
    session: Session, test_data: tuple[Galaxy, StarSystem, list[CelestialBody]]
):
    galaxy, _, _ = test_data
    statement = select(StarSystem).where(StarSystem.galaxy_id == galaxy.id)
    result = session.exec(statement).all()
    assert any(st.name == "Sol" for st in result)
    assert len(result) == 1


def test_query_star_system_bodies(
    session: Session, test_data: tuple[Galaxy, StarSystem, list[CelestialBody]]
):
    _, star_system, _ = test_data
    st = session.get(StarSystem, star_system.id)
    assert st is not None
    statement = select(CelestialBody).where(CelestialBody.star_system_id == st.id)
    bodies = session.exec(statement).all()
    names = {b.name for b in bodies}
    types = {b.type for b in bodies}
    assert "Earth" in names
    assert "Mars" in names
    assert "Sol" in names
    assert "planet" in types
    assert "star" in types
