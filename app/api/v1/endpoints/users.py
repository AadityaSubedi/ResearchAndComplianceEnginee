from fastapi import APIRouter, Request
from app.models.user import User

router = APIRouter()


@router.post("")
async def create_user(user: User):
    """Create a single User"""
    await user.insert()
    return user


@router.get("")
async def get_users(request: Request):
    """Get all users"""
    tenant_id = request.state.tenant_id
    return await User.find(User.tenant_id == tenant_id).to_list()
