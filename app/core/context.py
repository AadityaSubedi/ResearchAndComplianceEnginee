from contextvars import ContextVar
import contextvars
from typing import Optional


def set_context(context: str, value: str):
    """Set current tenant"""
    context_var: Optional[ContextVar[Optional[str]]] = None
    context_var_filter = list(
        filter(
            lambda key: key.name == context, contextvars.copy_context().keys()
        )
    )
    if context_var_filter:
        context_var = context_var_filter[0]
    else:
        context_var = ContextVar(context, default=None)

    context_var.set(value)


def get_context(context: str) -> str:
    """Get current tenant"""
    context_var_filter = list(
        filter(
            lambda key: key.name == context, contextvars.copy_context().keys()
        )
    )
    if not context_var_filter:
        raise RuntimeError(f"Contextvar `{context}` is not defined.")

    return context_var_filter[0].get()
