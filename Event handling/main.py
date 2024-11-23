from fastapi import FastAPI, Request


app = FastAPI()

@app.get("/")
async def main(request: Request):
	return { "message": "Welcome" }


@app.on_event("startup")
async def startup_event():
	print("SALOM men tug'ildim")

@app.on_event("shutdown")
async def shutdown_event():
	print("Xayr men o'ldim")
