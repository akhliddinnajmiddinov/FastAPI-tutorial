from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

@app.get('/{name}', response_class=HTMLResponse)
async def html(request: Request, name: str):
	return templates.TemplateResponse('index.html', {"request": request, "name": name})


if __name__ == "__main__":
	uvicorn.run('main2:app', host='localhost', port=1234, reload=True)