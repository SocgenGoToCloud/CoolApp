from typing import List

from fastapi.routing import APIRouter

from coolapi.models import CroissantRequest

router = APIRouter()


@router.get("")
def list_croissant_requests() -> List[CroissantRequest]:
    pass
