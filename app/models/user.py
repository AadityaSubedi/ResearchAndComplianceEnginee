from app.models.base import BaseDocument
from pymongo import IndexModel, ASCENDING
from enum import Enum, unique
from beanie import Indexed
from pydantic import Field
from typing import Annotated
from app.core.context import get_context

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
        
        indexes = [
            # Compound index for multi-tenant isolation
            IndexModel(
                [
                    ("org_id", ASCENDING), ("email", ASCENDING)
                ], unique=True
            ),
        ]
