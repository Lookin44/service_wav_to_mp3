from fastapi import FastAPI, HTTPException, status, Form, File, UploadFile
from fastapi.responses import FileResponse
from pydub import AudioSegment
from io import BytesIO

from data_base.db_serializers import *
from data_base.db_views import *


app = FastAPI()


@app.post(
    '/user_create',
    response_model=ResponseUser,
    status_code=status.HTTP_201_CREATED,
)
async def user_create(request: RequestUser):
    user_name = request.name
    user_exist = get_user_by_name(name=user_name)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'error': 'User already exist'},
        )
    new_user = set_user(name=user_name)
    return new_user


@app.post(
    '/audio_upload',
    status_code=status.HTTP_201_CREATED,
)
async def upload_audio(
        user_id: int = Form(...),
        access_token: str = Form(...),
        audio_file: UploadFile = File(...)
):

    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'error': 'User does not exist'},
        )
    if access_token != user.access_token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'error': 'Incorrect access_token'},
        )

    temp_file = set_audio_file(user_id)


    wav_data = BytesIO(audio_file.file.read())
    audio = AudioSegment.from_file(wav_data, format='wav')
    mp3_data = BytesIO()
    audio.export(mp3_data, format='mp3')

    with open(f'./media/{temp_file.id}.mp3', 'wb') as f:
        f.write(mp3_data.getvalue())
    url = f'http://127.0.0.1:8000/record?id={temp_file.id}&user={user_id}'

    return {'message': url}


@app.get(
    '/record',
    status_code=status.HTTP_200_OK,
)
async def download_audio(file_id: str, user_id: str):
    audio_file = get_audio_file_by_id(file_id)
    if not audio_file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': 'Audio file not found'},
        )

    user = get_user_by_id(int(user_id))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'error': 'User does not exist'},
        )

    path = f'./media/{file_id}.mp3'
    return FileResponse(path=path)
