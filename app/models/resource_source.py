import datetime
from enum import unique
from pydantic import Field, BaseModel
from pymongo import IndexModel, ASCENDING
from app.models.base import BaseDocument
from app.core.context import get_context


class Provenance(BaseModel):
    """Provenance"""
    page: int
    file_hash: str
    source_type: str


class ResearchSource(BaseDocument):
    """Resource Source"""
    
    content: str
    metadata: Provenance
    trust_level: int = Field(default=3, ge=1, le=5)  # 1=low, 5=high
    created_by: str = Field(default_factory=lambda: get_context("user_id"))
    
    class Settings:
        """Settings"""
        name = "research_sources"

        indexes = [
            # Leftmost tenant isolation index
            IndexModel(
                [("tenant_id", ASCENDING), ("_id", ASCENDING)]
            ),
            # Provenance index for grounding lookups
            IndexModel(
                [("tenant_id", ASCENDING), ("metadata.file_hash", ASCENDING)], unique=True
            ),
        ]
