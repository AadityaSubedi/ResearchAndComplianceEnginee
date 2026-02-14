from app.models.base import BaseDocument


class User(BaseDocument):  # pylint: disable=too-many-ancestors
    """User schema"""
    email: str
    full_name: str

    class Settings:
        """Settings"""
        name: str = "users"
