from fastapi import APIRouter, Depends

from app.api.v1.endpoints import health, users, documents
from app.middleware.jwt_middleware import require_jwt

protected_api_router = APIRouter(dependencies=[Depends(require_jwt)])

public_api_router = APIRouter()


public_api_router.include_router(
    health.router,
    prefix="/health",
    tags=["Health"],
)

protected_api_router.include_router(
    users.router,
    prefix="/users",
    tags=["Users"],
)

protected_api_router.include_router(
    documents.router,
    prefix="/documents",
    tags=["Documents"],
)

