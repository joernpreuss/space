from sqlmodel import Session, select

from backend.models import Galaxy, Planet, StarSystem


def test_planet_star_system_relation(
    session: Session, test_data: tuple[Galaxy, StarSystem, list[Planet]]
):
    _, star_system, _ = test_data
    statement = select(Planet).where(Planet.star_system_id == star_system.id)
    result = session.exec(statement).all()
    planet_names = {planet.name for planet in result}
    assert "Earth" in planet_names
    assert "Mars" in planet_names
    assert len(result) == 2


def test_star_system_galaxy_relation(
    session: Session, test_data: tuple[Galaxy, StarSystem, list[Planet]]
):
    galaxy, _, _ = test_data
    statement = select(StarSystem).where(StarSystem.galaxy_id == galaxy.id)
    result = session.exec(statement).all()
    assert any(st.name == "Sol" for st in result)
    assert len(result) == 1


def test_query_star_system_planets(
    session: Session, test_data: tuple[Galaxy, StarSystem, list[Planet]]
):
    _, star_system, _ = test_data
    st = session.get(StarSystem, star_system.id)
    assert st is not None
    statement = select(Planet).where(Planet.star_system_id == st.id)
    planets = session.exec(statement).all()
    names = {p.name for p in planets}
    assert names == {"Earth", "Mars"}
