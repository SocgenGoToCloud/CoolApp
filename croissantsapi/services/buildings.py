from typing import List

from croissantsapi.database.connector import ENGINE
import croissantsapi.database.models as db_models
from croissantsapi.errors.buildings import UnknownBuilding
from croissantsapi.models.buildings import Building


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


def get_building(building_id: str) -> Building:
    with ENGINE.scoped_session() as session:
        db_building = (
            session.query(db_models.Buildings)
            .filter(db_models.Buildings.id == building_id)
            .one_or_none()
        )
        if db_building is None:
            raise UnknownBuilding(building_id)
        return _building_from_db(db_building)
