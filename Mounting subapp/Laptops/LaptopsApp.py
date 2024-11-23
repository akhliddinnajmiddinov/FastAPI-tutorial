from fastapi import FastAPI

LaptopsApp = FastAPI()

@LaptopsApp.get("/")
async def main():
	return {"message": "LaptopsApp"}