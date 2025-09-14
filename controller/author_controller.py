from fastapi import APIRouter

router= APIRouter()

@router.post("/author")
async def create_author(data: dict):
    return {"Message": "Created"}

@router.get("/author/{author_id")
async def get_author(author_id: int):
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