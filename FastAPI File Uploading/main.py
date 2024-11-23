from fastapi import FastAPI, File, UploadFile
import uvicorn
import shutil

app = FastAPI()

@app.post("/uploader/")
async def UploadFile(file:UploadFile = File()):
    with open("dest.jpg", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {
        "filename": file.filename
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=1234, reload=True)