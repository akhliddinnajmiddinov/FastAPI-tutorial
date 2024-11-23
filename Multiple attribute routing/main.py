from fastapi import FastAPI
from models import User
import uvicorn

app = FastAPI()

@app.get('/')
async def index():
    """Main index funtion"""

    return {"name": "Joker"}


@app.get('/{name}/{age}')
async def secondView(name: str, age: int):
    data = {"name": name, "age": age}
    try: 
        User.model_validate(data)
        return data
    except:
        return {"error": True}


if __name__ == "__main__":
    uvicorn.run("main:app", host = "localhost", port = 1234, reload = True)