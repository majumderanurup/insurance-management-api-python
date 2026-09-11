from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.customer import AppException


def application_exception_handler(
    request: Request,
    exc: AppException,
):
    request_id = request.state.request_id

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": str(exc),
            "request_id": request_id,
        },
        headers={
            "X-Request-ID": request_id,
        },
    )