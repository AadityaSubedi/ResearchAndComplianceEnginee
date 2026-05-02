from fastapi import APIRouter, HTTPException
from app.models.user import User
from pymongo.errors import DuplicateKeyError

router = APIRouter(dependencies=[])


@router.post("")
async def create_user(user: User):
    """Create a single User"""
    try:
        await user.insert()
    except DuplicateKeyError as exc:
        raise HTTPException(
            status_code=400, detail="User with this email already exists."
        ) from exc

    return user


@router.get("")
async def get_users():
    """Get all users"""
    
    return await User.find().to_list()
