from functools import lru_cache
import asyncio

@lru_cache(maxsize=100)
async def get_factorial(n: int):
    await asyncio.sleep(2)
    if n == 1:
        return 1
    return n * await get_factorial(n-1)