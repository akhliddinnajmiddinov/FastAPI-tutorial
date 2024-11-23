from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
origins = [
    'http://localhost',
    'http://localhost:8080',
    'http://127.0.0.:8000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
    )


@app.get('/')
async def index():
    return {'message': 'hello'}

if __name__ == "__main__":
    uvicorn.run('main:app', host='localhost', port=1234, reload=True)