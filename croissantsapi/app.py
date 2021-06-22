from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from croissantsapi.routes.buildings import router as buildings_router
from croissantsapi.routes.croissants import router as croissants_router

app = FastAPI(
    title="CroissantsAPI", version="0.1.0", description="The coolest API in the world"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(croissants_router, prefix="/croissants", tags=["croissants"])
app.include_router(buildings_router, prefix="/buildings", tags=["buildings"])
