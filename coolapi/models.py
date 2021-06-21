from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class SocieteGeneraleBuilding(Enum):
    Chassagne = "Chassagne"
    Basalte = "Basalte"
    Alicante = "Alicante"
    Granite = "Granite"
    ValDeFontenay = "ValDeFontenay"


@dataclass
class DeliveryLocation:
    building: SocieteGeneraleBuilding
    floor: int
    room: int


@dataclass
class CroissantRequest:
    amount: int
    location: DeliveryLocation
    time: datetime
