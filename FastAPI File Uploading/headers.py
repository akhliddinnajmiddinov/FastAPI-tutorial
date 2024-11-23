from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse
from typing import Optional
import uvicorn

app = FastAPI()


@app.get('/headers/')
async def getHeader(accept_language:Optional[str]=Header(None)):
    return {
        "Accept-Language": accept_language
    }
    

@app.get('/rsheaders/')
async def resHeader():
    content = {
        "Message": "Hello"
    }
    headers = {"X-backend-framework": "flask", "Content-Language": "Uz"}
    response = JSONResponse(content=content, headers=headers)
    return response


if __name__ == "__main__":
    uvicorn.run("headers:app", host="localhost", port=1234, reload=True)