from contextvars import ContextVar
from typing import Optional

tenant_context: ContextVar[Optional[str]] = ContextVar("tenant_id", default=None)


def set_current_tenant(tenant_id: str):
    """Set current tenant"""
    tenant_context.set(tenant_id)


def get_current_tenant() -> str:
    """Get current tenant"""
    tenant = tenant_context.get()
    if tenant is None:
        raise RuntimeError("Tenant not set in context")
    return tenant
