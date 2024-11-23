from fastapi import FastAPI, Path, Query
from typing import Optional
import uvicorn
app = FastAPI()

@app.get("/salom/{name}")
async def salom(name:str=Path(min_length = 3, max_length = 5), age:int=Query(ge=1, le=5), course: Optional[float] = 5):
    return {
        "name": name,
        "age": age,
        "course": course
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=1234, reload=True)