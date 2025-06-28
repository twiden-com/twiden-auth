from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from src.api.v1.auth_routes import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from src.config.settings import settings
from src.config.container import get_container
from src.config.database import close_db_connections
from fastapi.responses import JSONResponse
import uvicorn 
import time
import logging

logging.basicConfig(
    level=getattr(logging, settings.log_level.upper()),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup - initialize dependencies
    container = get_container()
    await container.get_auth_controller()
    
    yield
    
    # Shutdown
    await close_db_connections()

app = FastAPI(
    title="Twiden Auth API",
    version="1.0.0",
    docs_url="/docs" if settings.environment == "dev" else None,  # Hide docs in prod
    redoc_url="/redoc" if settings.environment == "dev" else None,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

if settings.environment == "production":
    app.add_middleware(
        TrustedHostMiddleware, 
        allowed_hosts=["*"]
    )

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    logger.info(f"{request.method} {request.url.path}")
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"{response.status_code} - {duration:.3f}s")
    return response

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {str(exc)}")
    if settings.environment == "production":
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error"}
        )
    else:
        return JSONResponse(
            status_code=500,
            content={"detail": str(exc)}
        )

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "environment": settings.environment,
        "timestamp": time.time()
    }

@app.get("/")
def root():
    return {
        "message": "Twiden Auth API",
        "environment": settings.environment,
        "version": "1.0.0"
    }

app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.port,
        reload=settings.environment == "dev",
        workers=1 if settings.environment == "dev" else 4,
        log_level=settings.log_level.lower()
    )