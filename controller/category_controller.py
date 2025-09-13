from fastapi import FastAPI

app = FastAPI()

@app.post("/categories/{category_id}")
async def create_category(category_id: int):
    return {"Message": "Author"}

@app.get("/categories")
async def get_categories():
    return {"Message": "Categories"}

@app.get("/categories/{category_id}")
async def get_category(category_id: int):
    return {"Message": "Category"}

@app.put("/categories/{category_id}")
async def update_category(category_id: int, data: dict):
    return {"Message": "Updating"}

@app.delete("/categories/{category_id}")
async def delete_category(category_id: int):
    return {"Message": "Deleting"}