# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# import uvicorn


# app = FastAPI()

# @app.get('/')
# async def html(request: Request):
# 	res = """
# 	<html>
# 	<body>
# 	<h2>Hello World!</h2>
# 	</body>
# 	</html>
# 	"""
# 	return HTMLResponse(content=res)

# if __name__ == "__main__":
# 	uvicorn.run('main:app', host='localhost', port=1234, reload=True)