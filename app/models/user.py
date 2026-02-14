from app.models.base import BaseDocument
from enum import Enum

class RolesEnum(str, Enum): 
    """Roles enum"""
    OWNER = "owner"
    ADMIN = "admin"
    MEMBER = "member"


class User(BaseDocument):  # pylint: disable=too-many-ancestors
    """User schema"""
    email: str
    full_name: str
    role: RolesEnum

    class Settings:
        """Settings"""
        name: str = "users"
