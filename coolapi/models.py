from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel


@dataclass
class BuildingList:
    buildings: List[str]


@dataclass
class DeliveryLocation:
    building: str
    floor: int


@dataclass
class CroissantRequest:
    amount: int
    location: DeliveryLocation
    requester: str
    time: datetime
