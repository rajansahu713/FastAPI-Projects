from fastapi import FastAPI
from sse_starlette.sse import EventSourceResponse
import asyncio
import json

app = FastAPI()

async def event_generator():
    with open("scores.json", "r") as file:
        scores = json.load(file)
    for score in scores:
        await asyncio.sleep(5)  
        yield f"Match Summary: {json.dumps(score)}\n\n"

@app.get("/live-scores")
async def live_scores_endpoint():
    return EventSourceResponse(event_generator())

# Adding CORS middleware
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



