from fastapi import FastAPI

from coolapi.routes.croissants import router as croissants_router

app = FastAPI()

app.include_router(croissants_router, prefix="/croissants")
