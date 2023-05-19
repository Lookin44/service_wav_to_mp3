from pydantic import BaseModel


class RequestUser(BaseModel):
    name: str


class ResponseUser(BaseModel):
    id: int
    access_token: str

    class Config:
        orm_mode = True
