from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI()

data = []

class Book(BaseModel):
    name: str = Field("Oq kema", max_length=100)
    author: str = Field("Chingiz Aytmatov", max_length=100)
    year: int = Field(5, gt=1500, lt=2024)


@app.post("/")
async def add_book(book: Book):
    data.append(book)
    return data

@app.get("/")
async def get_books():
    return data

@app.put("/{id}")
async def update_book(id: int, book: Book):
    data[id - 1] = book
    return data

@app.delete("/{id}")
async def delete_book(id: int):
    data.pop(id - 1)
    return data

if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=1234, reload=True)