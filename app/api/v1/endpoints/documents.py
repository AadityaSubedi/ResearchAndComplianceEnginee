from fastapi import APIRouter
from app.models.resource_source import ResearchSource



router = APIRouter(dependencies=[])


@router.post("")
async def create_research_source(source: ResearchSource):
    """Create a single Research Source"""

    await source.insert()
    return source


@router.get("")
async def get_resources():
    """Get all users"""
    
    return await ResearchSource.find().to_list()
