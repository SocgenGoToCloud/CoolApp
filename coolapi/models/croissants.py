from datetime import datetime

from pydantic import BaseModel

from coolapi.models.buildings import DeliveryLocation


class CroissantRequest(BaseModel):
    amount: int
    location: DeliveryLocation
    requester: str
    time: datetime
