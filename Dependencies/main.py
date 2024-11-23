from fastapi import FastAPI, Depends, HTTPException
import uvicorn

app = FastAPI()


async def dependency(id: int, name: str, age: int):
    return {
        "id": id,
        "name": name,
        "age": age
    }


# @app.get("/name/")
# async def name(dep: dependency = Depends(dependency)):
#     return dep


# @app.get("/surname/")
# async def name(dep: dependency = Depends(dependency)):
#     return dep


async def validateAge(dep: dependency = Depends(dependency)):
    if dep["age"] < 18:
        raise HTTPException(status_code=400, detail="You are not eligible")


@app.get("/name/", dependencies = [Depends(validateAge)])
async def name(dep: dependency = Depends(dependency)):
    return dep


@app.get("/surname/", dependencies = [Depends(validateAge)])
async def name(dep: dependency = Depends(dependency)):
    return dep


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=1234, reload=True)