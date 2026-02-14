from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException

class TenantMiddleware(BaseHTTPMiddleware):
    """Tenant Middleware"""

    async def dispatch(self, request: Request, call_next):
        # TODO: Get the tenant id from the token.
        
        tenant_id = request.headers.get("X-Tenant-ID")

        request.state.tenant_id = tenant_id
        response = await call_next(request)
        return response
