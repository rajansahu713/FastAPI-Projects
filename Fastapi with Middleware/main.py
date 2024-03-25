from fastapi import FastAPI,  Body
from middleware import MyMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import time

app = FastAPI()
my_middleware = MyMiddleware(some_attribute="some_attribute_here_if_needed")
app.add_middleware(BaseHTTPMiddleware, dispatch=my_middleware)


@app.post("/")
async def root(json_body: dict = Body(...)):
    time.sleep(6) # Simulating some heavy processing
    return {"message": "Hello World"}


