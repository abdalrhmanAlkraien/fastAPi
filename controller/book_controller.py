from fastapi import FastAPI

app = FastAPI()

@app.post("/books")
async def create_book(data: dict):
    return {"Message": "Creating book"}

app.get("/books")
async def get_books(author_id: int):
    return {"Message": "Getting books"}

app.get("/books/{book_id}")
async def get_book(book_id: int):
    return {
        "Message": "Getting books"
    }

@app.put("/books/{book_id}")
async def update_book(book_id: int, data: dict):
    return {"Message": "Updating book"}


@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    return {"Message": "Deleting book"}