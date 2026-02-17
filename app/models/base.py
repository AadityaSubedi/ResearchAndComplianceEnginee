import datetime 
from typing import Any
from beanie import Document
from beanie.odm.operators.find.logical import And
from pydantic import Field
from pymongo import IndexModel, ASCENDING

from app.core.context import get_context


class BaseDocument(Document):  # pylint: disable=too-many-ancestors
    """Base schema"""
    tenant_id: str = Field(default_factory=lambda: get_context("tenant_id"))
    created_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(datetime.UTC))

    class Settings:
        """Settings"""
        use_state_management: bool = True
        indexes = [
            # Compound index for multi-tenant isolation
            IndexModel(
                [
                    ("tenant_id", ASCENDING), ("_id", ASCENDING)
                ]
            ),
        ]
        
    # -----------------------------
    # GLOBAL FIND ENFORCEMENT
    # -----------------------------
    @classmethod
    def find(cls, *args: Any, **kwargs: Any):
        tenant_id = get_context("tenant_id")

        # Always enforce tenant filter
        if args:
            # Merge existing filter with tenant filter
            combined_filter = And(cls.tenant_id == tenant_id, *args)
            return super().find(combined_filter, **kwargs)

        return super().find(cls.tenant_id == tenant_id, **kwargs)

    # Disable find_all completely
    @classmethod
    def find_all(cls, *args: Any, **kwargs: Any):
        raise RuntimeError("find_all() is disabled in multi-tenant mode.")
