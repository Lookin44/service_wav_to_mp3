from sqlalchemy import cast, String
from sqlalchemy.dialects.postgresql import UUID

from .db_models import AudioFile, User
from .db_settings import session


def set_user(name: str) -> User:
    user = User(name=name)
    session.add(user)
    session.commit()
    return user


def get_user_by_name(name: str) -> User:
    return session.query(User).filter_by(name=name).first()


def get_user_by_uuid(uuid: str) -> User:
    return session.query(User).filter_by(access_token=uuid).first()


def get_user_by_id(id: int) -> User:
    return session.query(User).filter_by(id=id).first()


def set_audio_file(user_id: int) -> AudioFile:
    audio_file = AudioFile(user_id=user_id)
    session.add(audio_file)
    session.commit()
    return audio_file


def get_audio_file_by_id(id: str) -> AudioFile:
    return session.query(AudioFile).filter_by(id=id).first()
