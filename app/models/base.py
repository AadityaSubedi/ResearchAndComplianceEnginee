import datetime 
from beanie import Document
from pydantic import Field


class BaseDocument(Document):  # pylint: disable=too-many-ancestors
    """Base schema"""
    tenant_id: str
    created_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(datetime.UTC))

    class Settings:
        """Settings"""
        use_state_management: bool = True
