from pydantic import BaseModel

class BaseMessageResponse(BaseModel):
    message:str

class PayloadSchema(BaseModel):
    username: str
    password: str
    email: str

class UpdateResponseSchema(BaseMessageResponse):
    payload:PayloadSchema
