from fastapi import FastAPI
from decorators import cache_decorator, cache
from functools_caching import get_factorial

app = FastAPI()


# Define your data processing function with the caching decorator
@app.post("/data")
@cache_decorator(expire=3600)
def get_data(body: dict):
    # performing operations
       
    processed_data = body
    
    # For demonstration, we're just returning the input
    return processed_data

@app.get("/clear-cache")
def clear_cache():
    cache.clear()
    return {"message": "Cache invalidated"}


@app.get("/factorial/{num}")
async def compute(num: int):
    result = await get_factorial(num)
    return {"param": num, "result": result}