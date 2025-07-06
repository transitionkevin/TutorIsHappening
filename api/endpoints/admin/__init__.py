from fastapi import APIRouter
from typing import Union
from api.schemas.common_schema import BaseMessageResponse,PayloadSchema, UpdateResponseSchema
from tools.utils import is_valid_email, hash_password

admin_router = APIRouter(prefix="/admin", tags=["Admin"])

@admin_router.get("/status")
async def admin_status():
    return {"message": "Admin server is healthy"}


@admin_router.post("/create_user",response_model=Union[BaseMessageResponse,UpdateResponseSchema])
async def create_user(payload:PayloadSchema):
    username = payload.username
    password = payload.password
    email = payload.email

    if not is_valid_email(email):
        out={"message": "not success"}
        return BaseMessageResponse(**out)

    password_hash =  hash_password(password)

    userinput ={
        "username":username,
        "password":password_hash,
        "email":email
    }
    return UpdateResponseSchema(**{"message": "success", "payload": userinput})