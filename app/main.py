from fastapi import FastAPI
from app.config.settings import settings
from app.core.logging import setup_logging
from app.api.v1.router import router as api_router

setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": settings.APP_NAME,
        "env": settings.APP_ENV
    }
