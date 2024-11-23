from fastapi.responses import HTMLResponse
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/hello/", response_class=HTMLResponse)
def hello():
    res = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    SALOM MENING DO'stim
</body>
</html>"""
    return HTMLResponse(content=res)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=1234, reload=True)