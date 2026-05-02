from app.models.base import BaseDocument
from enum import Enum
from pydantic import Field

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
    user_id: str = Field(default_factory=lambda: get_context("user_id"))

    class Settings:
        """Settings"""
        name: str = "users"
