from typing import Annotated

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from fastapi.params import Depends

from config.container_config import Container
from schema.request.AuthorRequest import AuthorRequest
from service.author_service import AuthorService
router= APIRouter()

@router.post("/author")
@inject
async def create_author(authorRequest:AuthorRequest, author_service:Annotated[
    AuthorService,
    Depends(Provide[Container.auth_service])
]):
    author_service.create_author(authorRequest)
    return {"Message": "Created"}

@router.get("/author/{author_id}")
@inject
async def get_author(author_id: int, author_service:Annotated[
    AuthorService,
    Depends(Provide[Container.auth_service])
]):
    return author_service.find_author_by_id(author_id)

@router.get("/authors")
@inject
async def get_authors(author_service:Annotated[
    AuthorService,
    Depends(Provide[Container.auth_service])
]):

    return author_service.find_all_author()

@router.put("/authors/{author_id}")
@inject
async def update_author(author_id: int, data:AuthorRequest, author_service:Annotated[
    AuthorService,
    Depends(Provide[Container.auth_service])
]):
    author_service.update_author(author_id, data)
    return {"Message": "Updated"}

@router.delete("/authors/{author_id}")
@inject
async def delete_author(author_id: int, author_service:Annotated[
    AuthorService,
    Depends(Provide[Container.auth_service])
]):
    author_service.delete_author(author_id)
    return {"Message": "Deleted"}

