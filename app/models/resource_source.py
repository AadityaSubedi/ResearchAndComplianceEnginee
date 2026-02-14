import datetime
from pydantic import Field, BaseModel
from pymongo import IndexModel, ASCENDING
from app.models.base import BaseDocument


class Provenance(BaseModel):
    """Provenance"""
    page: int
    file_hash: str
    source_type: str


class ResearchSource(BaseDocument):
    """Resource Source"""
    content: str
    metadata: Provenance
    ingested_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(datetime.UTC))
    
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
                [("tenant_id", ASCENDING), ("metadata.file_hash", ASCENDING)]
            ),
        ]
