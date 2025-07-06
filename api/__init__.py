from fastapi import APIRouter,FastAPI
from api.endpoints import admin_router
from api.endpoints import user_router

def include_routers(app: FastAPI):
    router = APIRouter()
    router.include_router(user_router)
    router.include_router(admin_router)

    app.include_router(router)