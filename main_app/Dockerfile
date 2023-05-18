FROM python:3.11.2-alpine

LABEL authors="egor"

WORKDIR /usr/src/main_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add ffmpeg

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
