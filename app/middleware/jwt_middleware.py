from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
from app.core.context import set_context, get_context
from utilities.jwt_token import JWTManager


class JWTMiddleware(BaseHTTPMiddleware):
    """JWT MiddleWare"""

    async def dispatch(self, request: Request, call_next):

        jwt_manager = JWTManager(request)
        jwt_manager.verify_jwt_in_request()

        payload = jwt_manager.claims

        # Extract tenant_id + user_id
        org_id, user_id = None, None
        if isinstance(payload, dict):
            org_id = payload.get("org_id")
            user_id = payload.get("user_id")

        if not org_id or not user_id:
            raise HTTPException(
                status_code=401, detail="Token missing tenant or user info"
            )

        # Inject into context
        set_context(org_id=org_id, user_id=user_id)

        response = await call_next(request)
        return response
    
    
async def require_jwt(request: Request):
    """Dependency to require JWT in routes"""
    jwt_manager = JWTManager(request)
    jwt_manager.verify_jwt_in_request()

    payload = jwt_manager.claims

    # Extract tenant_id + user_id
    org_id, user_id = None, None
    if isinstance(payload, dict):
        org_id = payload.get("org_id")
        user_id = payload.get("user_id")

    if not org_id or not user_id:
        raise HTTPException(
            status_code=401, detail="Token missing tenant or user info"
        )

    # Inject into context
    set_context(org_id=org_id, user_id=user_id)
    # Inject into the request state for future use in the route handlers
    request.state.org_id = org_id
    request.state.user_id = user_id
    
    return

