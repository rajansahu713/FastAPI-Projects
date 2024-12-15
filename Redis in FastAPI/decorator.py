from functools import wraps
from hashlib import sha256
import json
import redis


redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

app_cache_key = "app_cache"

# Cache decorator
def cache_decorator(expire=3600):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Create a unique cache key based on function name and parameters
            key = sha256(json.dumps((func.__name__, args, kwargs), sort_keys=True).encode()).hexdigest()
            cached_data = redis_client.get(f"{key}_{app_cache_key}")
            if cached_data:
                # Deserialize cached data
                return json.loads(cached_data)

            # Await the result of the async function
            result = await func(*args, **kwargs)

            # Serialize and cache the result
            redis_client.set(f"{key}_{app_cache_key}", json.dumps(result), ex=expire)
            return result

        return wrapper

    return decorator



