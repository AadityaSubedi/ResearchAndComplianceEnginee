from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.api import api_router
from app.db.database import init_db
from app.middleware.tenant import TenantMiddleware


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Startup operatioons
    await init_db()
    
    yield
    # Shutdown operations

app = FastAPI(title="Research API", lifespan=lifespan)

app.add_middleware(TenantMiddleware)

app.include_router(api_router, prefix="/api/v1")

