from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Tuple
import uvicorn

app = FastAPI()

# class Student(BaseModel):
#     id: int = 5
#     name: str = Field("Ahliddin", title="Enter student name", max_length=10)
#     marks: List[int]
#     persentMark: float

# class Percent(BaseModel):
#     id: int
#     name: str = Field(None, title="Enter student name", max_length=10)
#     persentMark: float
    
    
# @app.post("/student/", response_model=Percent)
# async def resModel(student: Student):
#     student.persentMark = sum(student.marks) / 2
#     return student



# NESTED models
class supplier(BaseModel):
   supplierID:int
   supplierName:str
class product(BaseModel):
   productID:int
   prodname:str
   price:int
   supp:supplier
class customer(BaseModel):
   custID:int
   custname:str
   prod:Tuple[product]


@app.post("/customer")
async def Customer(cs: customer):
    return cs


if __name__ == "__main__":
    uvicorn.run("response_model:app", host="localhost", port=1234, reload=True)