from pydantic import BaseModel, validator


class GeneralUser(BaseModel):
    name: str

    @validator('name')
    def name_check(cls, value: str):
        if type(value) != str:
            raise ValueError({'error': 'Name mast be string'})
        return value


class ResponseUser(BaseModel):
    id: int
    access_token: str

    class Config:
        orm_mode = True
