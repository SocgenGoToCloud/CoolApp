from coolapi.models.croissants import CroissantRequest
from typing import List

from fastapi.routing import APIRouter

from coolapi.models.buildings import BuildingList, Building
import coolapi.services.buildings as buildings_service

router = APIRouter()


@router.get("", response_model=BuildingList)
def list_buildings():
    return BuildingList(buildings=buildings_service.get_all_buildings())


@router.get("/{id}", response_model=Building)
def get_building(id: str):
    return buildings_service.get_building(id)
