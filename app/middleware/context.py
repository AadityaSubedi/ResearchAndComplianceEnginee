from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from app.core.context import set_context
import uuid


class RequestContextMiddleware(BaseHTTPMiddleware):
    """Tenant Middleware"""

    async def dispatch(self, request: Request, call_next):
        
        request_id = request.headers.get("X-Request-ID") or uuid.uuid4().hex
        
        # Set the tenant context
        set_context(request_id=request_id)

        response = await call_next(request)
        return response
