# Микросервис WAV to MP3

Этот микросервис написан на Python 3.11.2 с использованием следующих библиотек:
- FastAPI
- SQLAlchemy
- psycopg2-binary
- uvicorn
- pydub
- python-multipart

## Установка

1. Склонируйте репозиторий на свой сервер:
```git
git clone https://github.com/Lookin44/service_wav_to_mp3.git
```

2. Перейдите в директорию склонированного репозитория:
```shell
cd path/to/directory/service_wav_to_mp3
```

3. Создайте файл `.env` со следующими данными:
```dotenv
PSQL_DATABASE=your_db_name
PSQL_USER=your_db_username
PSQL_PASSWORD=your_db_password
```

4. Запустите Docker Compose:
```docker
docker-compose up -d
```

## Работа с микросервисом

Вы можете выполнять запросы через встроенный OpenAPI или используя Postman.

### Регистрация пользователя

Выполните POST-запрос на адрес `http://127.0.0.1:8000/user_create` с телом 
запроса в формате JSON:
```json
{
  "name": "your_name"
}
```

В ответ получите объект с идентификатором пользователя и токеном доступа:
```json
{
  "id": 1,
  "access_token": "be71e2a4-3ab5-4796-bc35-4eb4eb5e5573"
}
```


### Конвертация WAV в MP3

Выполните POST-запрос на адрес `http://127.0.0.1:8000/audio_upload` со следующими данными:
- `user_id`: идентификатор пользователя
- `access_token`: токен доступа
- `audio_file`: аудиозапись в формате WAV

В ответ получите ссылку на скачивание MP3 файла:
```json
{
  "message": "http://127.0.0.1:8000/record?id=9a32fc53-4b39-43ba-b0d4-fe4133bf0908&user=1"
}
```


### Скачивание MP3 файла

Выполните GET-запрос на адрес `http://127.0.0.1:8000/record?id=9a32fc53-4b39-43ba-b0d4-fe4133bf0908&user=1`, где `id` и `user` - параметры, полученные ранее. В ответ будет скачан MP3 файл.

