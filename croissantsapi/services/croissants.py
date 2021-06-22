from datetime import time
from typing import List

from croissantsapi.database.connector import ENGINE
import croissantsapi.database.models as db_models
from croissantsapi.errors.buildings import UnknownBuilding, BuildingFloorOverflow
from croissantsapi.errors.croissants import UnknownCroissantRequest
from croissantsapi.models.buildings import DeliveryLocation
from croissantsapi.models.croissants import CroissantRequest, NewCroissantRequest


def _croissant_from_db(croissant: db_models.CroissantsRequests) -> CroissantRequest:
    with ENGINE.scoped_session() as session:
        return CroissantRequest(
            id=croissant.id,
            amount=croissant.amount,
            requester=croissant.requester,
            location=DeliveryLocation(
                building=croissant.building, floor=croissant.floor
            ),
            time=croissant.time,
        )


def get_all_croissant_requests() -> List[CroissantRequest]:
    with ENGINE.scoped_session() as session:
        db_croissants = session.query(db_models.CroissantsRequests).all()
        return [_croissant_from_db(croissant) for croissant in db_croissants]


def get_croissant_request(request_id: int) -> CroissantRequest:
    with ENGINE.scoped_session() as session:
        db_croissant = (
            session.query(db_models.CroissantsRequests)
            .filter(db_models.CroissantsRequests.id == request_id)
            .one_or_none()
        )
        if db_croissant is None:
            raise UnknownCroissantRequest(request_id)
        return _croissant_from_db(db_croissant)


def create_croissant_request(request: NewCroissantRequest) -> CroissantRequest:
    with ENGINE.scoped_session() as session:
        db_building = (
            session.query(db_models.Buildings)
            .filter(db_models.Buildings.id == request.location.building)
            .one_or_none()
        )
        if db_building is None:
            raise UnknownBuilding(request.location.building)
        if request.location.floor > db_building.max_floors:
            raise BuildingFloorOverflow(
                request.location.building,
                request.location.floor,
                db_building.max_floors,
            )
        new_request = db_models.CroissantsRequests(
            requester=request.requester,
            amount=request.amount,
            building=request.location.building,
            floor=request.location.floor,
            time=request.time,
        )
        session.add(new_request)
        session.commit()
        return _croissant_from_db(new_request)


def delete_croissant_request(request_id: int):
    with ENGINE.scoped_session() as session:
        db_request = (
            session.query(db_models.CroissantsRequests)
            .filter(db_models.CroissantsRequests.id == request_id)
            .one_or_none()
        )
        if db_request is None:
            raise UnknownCroissantRequest(request_id)
        session.delete(db_request)
        session.commit()
