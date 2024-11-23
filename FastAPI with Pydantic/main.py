from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import List
import uvicorn

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str=Field(None, title = "Enter the name", max_length=10)
    subjects: List[str] = []
    
    
# @app.post("/students/")
# async def students(student: Student):
#     return student


# @app.post("/students/")
# async def students(id: int=Body(), name: str=Body(), subjects:List[str]=Body()):
#     return {
#         "id": id,
#         "name": name,
#         "subjects": subjects
#     }


# @app.post("/students/{title}")
# async def students(title:str, code: int, id: int=Body(), name: str=Body(), subjects:List[str]=Body()):
#     return {
#         "id": id,
#         "name": name,
#         "subjects": subjects
#     }


@app.post("/students/{title}")
async def students(title:str, code: int, student: Student):
    return student


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=1234, reload=True)