import asyncio
import json
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import redis.asyncio as aioredis

REDIS_URL = "redis://localhost:6379/0"
CHANNEL = "ipl-score"

app = FastAPI(title="Live IPL Score Streaming")

redis_client = None
client_queues = set()


async def redis_listener():
    pubsub = redis_client.pubsub(ignore_subscribe_messages=True)
    await pubsub.subscribe(CHANNEL)

    async for message in pubsub.listen():
        data = message["data"]
        if isinstance(data, bytes):
            data = data.decode()

        for q in list(client_queues):
            try:
                q.put_nowait(data)
            except asyncio.QueueFull:
                pass


@app.on_event("startup")
async def startup():
    global redis_client
    redis_client = aioredis.from_url(REDIS_URL)
    asyncio.create_task(redis_listener())


async def event_stream(request: Request, queue: asyncio.Queue):
    while True:
        if await request.is_disconnected():
            break

        try:
            msg = await asyncio.wait_for(queue.get(), timeout=15)
        except asyncio.TimeoutError:
            yield ":\n\n"
            continue

        yield f"data: {msg}\n\n"


@app.get("/live-score")
async def live_score(request: Request):
    q = asyncio.Queue(maxsize=100)
    client_queues.add(q)

    return StreamingResponse(
        event_stream(request, q),
        media_type="text/event-stream"
    )


@app.get("/")
async def home():
    return {"message": "Connect to /live-score for live IPL updates"}
