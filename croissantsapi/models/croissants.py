from datetime import datetime
from typing import List

from pydantic import BaseModel

from croissantsapi.models.buildings import DeliveryLocation


class CroissantRequest(BaseModel):
    id: int
    amount: int
    location: DeliveryLocation
    requester: str
    time: datetime


class NewCroissantRequest(BaseModel):
    amount: int
    location: DeliveryLocation
    requester: str
    time: datetime


class CroissantRequests(BaseModel):
    requests: List[CroissantRequest]
