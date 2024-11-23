from fastapi import FastAPI
from Books.BooksApp import BooksApp
from Laptops.LaptopsApp import LaptopsApp

app = FastAPI()

app.mount("/books", BooksApp)
app.mount("/laptops", LaptopsApp)
