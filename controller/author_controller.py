from typing import Annotated

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from fastapi.params import Depends

from config.container_config import Container
from service.author_service import AuthorService

router= APIRouter()

@router.post("/author")
@inject
async def create_author(data: dict, author_service:Annotated[
    AuthorService,
    Depends(Provide[Container.auth_service])
]):
    author_service.create_author(data)
    return {"Message": "Created"}

@router.get("/author/{author_id")
@inject
async def get_author(author_id: int, author_service:Annotated[
    AuthorService,
    Depends(Provide[Container.auth_service])
]):
    author_service.get_author(author_id)
    return {"Message": "Author"}

@router.get("/authors")
async def get_authors():
    return {"Message": "Authors"}

@router.put("/authors/{author_id}")
async def update_author(author_id: int, data: dict):
    return {"Message": "Updated"}

@router.delete("/authors/{author_id}")
async def delete_author(author_id: int):
    return {"Message": "Deleted"}