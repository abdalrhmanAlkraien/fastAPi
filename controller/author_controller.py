from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.post("/author")
async def create_author(data: dict):
    return {"Message": "Created"}

@app.get("/author/{author_id")
async def get_author(author_id: int):
    return {"Message": "Author"}

@app.get("/authors")
async def get_authors():
    return {"Message": "Authors"}

@app.put("/authors/{author_id}")
async def update_author(author_id: int, data: dict):
    return {"Message": "Updated"}

@app.delete("/authors/{author_id}")
async def delete_author(author_id: int):
    return {"Message": "Deleted"}