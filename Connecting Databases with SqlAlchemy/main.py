from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from fastapi import FastAPI, Depends
from typing import List
import uvicorn

DATABASE_URL = "postgresql+psycopg2://postgres:1423@localhost:5432/sqlalchemy"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Books(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), unique=True)
    author = Column(String(50))
    year = Column(Integer)

    def __str__(self):
        return self.title

Base.metadata.create_all(bind=engine)


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    class Config:
        from_attributes = True


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

# print(*session().query(Books).all())

@app.post("/", response_model=Book)
async def add_book(b1: Book, db: Session = Depends(get_db)):
    bk = Books(id=b1.id, title=b1.title, author=b1.author, year=b1.year)
    db.add(bk)
    db.commit()
    db.refresh(bk)
    return Books(**b1.dict())


@app.get("/list", response_model=List[Book])
async def get_books(db: Session = Depends(get_db)):
    books = db.query(Books).all()
    return books


@app.put('/put', response_model=Book)
async def update_book(book: Book, db: Session = Depends(get_db)):
    book_orig = db.query(Books).filter(Books.id == book.id).first()
    book_orig.title = book.title
    book_orig.author = book.author
    book_orig.year = book.year
    print(book_orig)
    db.commit()
    return book


@app.delete('/delete/{id}', response_model=Book)
async def update_book(id: int, db: Session = Depends(get_db)):
    book = db.query(Books).filter(Books.id == id).first()
    db.delete(book)
    db.commit()
    return book


if __name__ == "__main__":
    uvicorn.run('main:app', host='localhost', port=1234, reload=True)
