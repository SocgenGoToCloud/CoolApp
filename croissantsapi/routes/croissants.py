from typing import List

from fastapi.routing import APIRouter

from croissantsapi.models.croissants import (
    CroissantRequests,
    CroissantRequest,
    NewCroissantRequest,
)
import croissantsapi.services.croissants as croissants_service

router = APIRouter()


@router.get("", response_model=CroissantRequests)
def list_croissant_requests():
    return CroissantRequests(requests=croissants_service.get_all_croissant_requests())


@router.get("/{id}", response_model=CroissantRequests)
def get_croissant_request(id: int):
    return croissants_service.get_croissant_request(id)


@router.post("", response_model=CroissantRequest)
def create_croissant_request(request: NewCroissantRequest):
    return croissants_service.create_croissant_request(request)


@router.delete("/{id}")
def delete_croissant_request(id: int):
    croissants_service.delete_croissant_request(id)
