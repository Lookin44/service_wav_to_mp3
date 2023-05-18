from .db_models import User
from .db_settings import session


def set_user(name: str) -> User:
    user = User(name=name)
    session.add(user)
    session.commit()
    return user
