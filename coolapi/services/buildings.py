from typing import List

from coolapi.database.connector import ENGINE
import coolapi.database.models as db_models
from coolapi.models.buildings import Building


def _building_from_db(building: db_models.Buildings) -> Building:
    with ENGINE.scoped_session() as session:
        return Building(
            id=building.id,
            name=building.name,
            max_floors=building.max_floors,
        )


def get_all_buildings() -> List[Building]:
    with ENGINE.scoped_session() as session:
        db_buildings = session.query(db_models.Buildings).all()
        return [_building_from_db(building) for building in db_buildings]
