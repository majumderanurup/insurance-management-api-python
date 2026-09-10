from fastapi import FastAPI

from app.core.config import settings
from app.db.base import Base
from app.db.database import engine
from app.models.customer import Customer
from app.routers.customer import router as customer_router
from app.routers.health import router as health_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(health_router)
app.include_router(customer_router)