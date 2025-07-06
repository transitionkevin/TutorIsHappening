from fastapi import APIRouter

user_router = APIRouter(prefix="/user", tags=["User"])

@user_router.get("/status")
async def user_status():
    return {"message": "User server is healthy"}




