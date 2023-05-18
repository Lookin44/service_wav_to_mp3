from fastapi import FastAPI, HTTPException

from data_base.db_serializers import GeneralUser, ResponseUser
from data_base.db_views import set_user


app = FastAPI()


@app.post('/user_create', response_model=ResponseUser)
async def user_create(name: GeneralUser):
    new_user = set_user(name=name.name)
    return new_user
