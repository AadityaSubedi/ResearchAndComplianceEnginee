from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.core.config import settings
from app.models.user import User
from app.models.resource_source import ResearchSource

client = AsyncIOMotorClient(settings.MONGODB_URL)
db = client["research_db"]

async def init_db():
    """Init db"""
    await init_beanie(
        database=db,
        document_models=[User, ResearchSource],
    )
