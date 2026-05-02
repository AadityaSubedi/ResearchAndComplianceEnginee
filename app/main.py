from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.api import protected_api_router as api_router, public_api_router
from app.db.database import init_db
from app.middleware import RequestContextMiddleware


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Startup operatioons
    await init_db()
    
    yield
    # Shutdown operations

app = FastAPI(title="Research API", lifespan=lifespan)

app.add_middleware(RequestContextMiddleware)

app.include_router(public_api_router, prefix="/api/v1")
app.include_router(api_router, prefix="/api/v1")
