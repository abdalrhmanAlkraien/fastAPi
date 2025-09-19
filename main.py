# main.py
from fastapi import FastAPI

from config.container_config import Container
from controller import author_controller, book_controller, category_controller
from controller.author_controller import router as author_router
from controller.book_controller import router as book_router

app = FastAPI(title="Book Management API")
app.include_router(author_router, prefix="/api", tags=["Authors"])
app.include_router(book_router, prefix="/api", tags=["Books"])

container = Container()
container.wire(modules=[author_controller, book_controller, category_controller])
