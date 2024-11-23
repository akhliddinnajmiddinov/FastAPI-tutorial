from fastapi import FastAPI

BooksApp = FastAPI()

@BooksApp.get("/")
async def main():
	return {"message": "BooksAPP"}