from fastapi import FastAPI

from coolapi.routes.buildings import router as buildings_router
from coolapi.routes.croissants import router as croissants_router

app = FastAPI()

app.include_router(croissants_router, prefix="/croissants", tags=["croissants"])
app.include_router(buildings_router, prefix="/buildings", tags=["buildings"])
