from fastapi import FastAPI, HTTPException
import asyncio
from decorator import cache_decorator, redis_client

app = FastAPI()

@app.post("/get_details")
@cache_decorator(expire=3600)
async def get_details(body: dict):
    # Simulate a delay (e.g., for database query)
    await asyncio.sleep(2)
    return {"data": body}




@app.delete("/delete_keys_with_suffix/{suffix}")
async def delete_keys_with_suffix(suffix: str):
    # Use SCAN to find keys ending with the given suffix
    keys_to_delete = []
    cursor = 0
    while True:
        cursor, keys = redis_client.scan(cursor=cursor, match=f"*{suffix}")
        keys_to_delete.extend(keys)
        if cursor == 0:
            break

    # If no keys are found, raise an exception
    if not keys_to_delete:
        raise HTTPException(status_code=404, detail=f"No keys ending with '{suffix}' found")

    # Delete the keys
    deleted_count = redis_client.delete(*keys_to_delete)

    return {"message": f"Deleted {deleted_count} keys ending with '{suffix}'"}





