from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.customer import AppException


def application_exception_handler(
    request: Request,
    exc: AppException,
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": str(exc),
        },
    )