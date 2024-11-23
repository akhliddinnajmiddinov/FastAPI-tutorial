from pydantic import BaseModel

class User(BaseModel):
    name: str = "Ahliddin"
    age: int