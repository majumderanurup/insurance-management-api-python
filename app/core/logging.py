import logging
from pathlib import Path

from app.core.request_context import request_id_context


class RequestIdFilter(logging.Filter):

    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = request_id_context.get()
        return True


class RequestIdFormatter(logging.Formatter):

    def format(self, record: logging.LogRecord) -> str:
        request_id = getattr(record, "request_id", "-")
        record.request_id = request_id

        return super().format(record)


def configure_logging():
    log_directory = Path("logs")
    log_directory.mkdir(exist_ok=True)

    formatter = RequestIdFormatter(
        "%(asctime)s | %(levelname)s | %(name)s | "
        "request_id=%(request_id)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.addFilter(RequestIdFilter())

    file_handler = logging.FileHandler(
        log_directory / "app.log"
    )
    file_handler.setFormatter(formatter)
    file_handler.addFilter(RequestIdFilter())

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    root_logger.handlers.clear()
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    sqlalchemy_logger = logging.getLogger("sqlalchemy.engine")
    sqlalchemy_logger.handlers.clear()
    sqlalchemy_logger.propagate = True