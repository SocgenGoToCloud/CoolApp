from typing import List

from pydantic import BaseModel


class Building(BaseModel):
    id: str
    name: str
    max_floors: int


class BuildingList(BaseModel):
    buildings: List[Building]


class DeliveryLocation(BaseModel):
    building: str
    floor: int
