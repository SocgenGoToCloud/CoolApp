from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from coolapi.routes.buildings import router as buildings_router
from coolapi.routes.croissants import router as croissants_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(croissants_router, prefix="/croissants", tags=["croissants"])
app.include_router(buildings_router, prefix="/buildings", tags=["buildings"])
