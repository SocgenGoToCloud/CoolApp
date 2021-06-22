from coolapi.database.connector import ENGINE
from coolapi.database.models import Buildings

BUILDINGS = [
    Buildings(id="alicante", name="Alicante", max_floors=37),
    Buildings(id="chassagne", name="Chassagne", max_floors=36),
    Buildings(id="granite", name="Granite", max_floors=36),
    Buildings(id="basalte", name="Basalte", max_floors=5),
    Buildings(id="dunes", name="Les Dunes", max_floors=8),
]


def populate():
    with ENGINE.scoped_session() as session:
        for building in BUILDINGS:
            session.add(building)
            session.commit()
