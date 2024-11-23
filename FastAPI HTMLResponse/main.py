from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/hello/", response_class=HTMLResponse)
def hello(request: Request):
    return templates.TemplateResponse("index.html", request = request)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=1234, reload=True)