from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from .db_settings import engine


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    access_token = Column(
        String,
        nullable=False,
        unique=True,
        default=uuid4
    )


class AudioFile(Base):
    __tablename__ = 'audio_files'

    id = Column(String, primary_key=True, default=str(uuid4()))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User, backref='audios')


Base.metadata.create_all(engine)
