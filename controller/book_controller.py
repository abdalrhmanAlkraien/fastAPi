from fastapi import APIRouter

router = APIRouter()

@router.post("/books")
async def create_book(data: dict):
    return {"Message": "Creating book"}

@router.get("/books")
async def get_books(author_id: int):
    return {"Message": "Getting books"}

@router.get("/books/{book_id}")
async def get_book(book_id: int):
    return {
        "Message": "Getting books"
    }

@router.put("/books/{book_id}")
async def update_book(book_id: int, data: dict):
    return {"Message": "Updating book"}


@router.delete("/books/{book_id}")
async def delete_book(book_id: int):
    return {"Message": "Deleting book"}