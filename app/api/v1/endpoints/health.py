from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def health_check():
    """Check the health of the application"""
    return {"status": "healthy"}

