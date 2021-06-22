from typing import List

from fastapi.routing import APIRouter

from coolapi.models.buildings import BuildingList
import coolapi.services.buildings as buildings_service

router = APIRouter()


@router.get("")
def list_buildings() -> BuildingList:
    return BuildingList(buildings=buildings_service.get_all_buildings())
