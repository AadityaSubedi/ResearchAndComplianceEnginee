from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from app.core.tenant_context import set_current_tenant


class TenantMiddleware(BaseHTTPMiddleware):
    """Tenant Middleware"""

    async def dispatch(self, request: Request, call_next):
        
        # TODO: Get the tenant id from the token.
        tenant_id = request.headers.get("X-Tenant-ID", "")
        
        set_current_tenant(tenant_id)

        request.state.tenant_id = tenant_id
        response = await call_next(request)
        return response
