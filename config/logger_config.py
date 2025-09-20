import logging

# 1. configure root logger before Uvicorn starts
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

log = logging.getLogger("book_app")  # use a named logger