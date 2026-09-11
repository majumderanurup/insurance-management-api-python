from fastapi import FastAPI

from app.core.config import settings
from app.db.base import Base
from app.db.database import engine
from app.exceptions.customer import AppException
from app.handlers.exceptions import application_exception_handler
from app.routers.customer import router as customer_router
from app.routers.health import router as health_router
from app.core.logging import configure_logging
from app.middleware.request_id import request_id_middleware


Base.metadata.create_all(bind=engine)

configure_logging()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.add_exception_handler(
    AppException,
    application_exception_handler,
)

app.middleware("http")(request_id_middleware)

app.include_router(health_router)
app.include_router(customer_router)