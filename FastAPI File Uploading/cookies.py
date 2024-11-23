from fastapi import FastAPI, Cookie
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()


@app.post("/create_cookie/")
async def createCookie():
    content = {
        "success": "Cookie was setted"
    }
    response = JSONResponse(content=content)
    response.set_cookie("username", "Ahliddin")
    return response
    

@app.get("/read_cookie/")   
async def readCookie(username:str = Cookie(None)): 
    return {
        "username": username
    }


if __name__ == "__main__":
    uvicorn.run("cookies:app", host="localhost", port=1234, reload=True)