"""Authentication and authorization"""
import datetime
from jose import jwt
from app.core.config import settings


def create_access_token(data: dict, expires_delta: int = 60):
    """Creates an access token."""
    expire = datetime.datetime.now(tz=datetime.UTC) + datetime.timedelta(minutes=expires_delta)
    to_encode = {**data, "exp": expire}

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )
    return encoded_jwt
