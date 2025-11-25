# FastAPI + Redis Pub/Sub

A minimal example project showing how to integrate Redis Pub/Sub with a FastAPI app. This repository demonstrates publishing messages to Redis from HTTP endpoints and delivering messages to subscribers via HTTP/Server-Sent Events (SSE) or WebSockets.


## Features
- Publish messages into Redis channels
- Subscribe to messages using SSE or WebSockets


## Prerequisites
- Python 3.9+ (3.11 recommended)
- Redis server (local or Docker)
- Poetry or pip for dependencies
- Optional: Docker & docker-compose

## Environment Variables
- REDIS_URL (default: redis://localhost:6379/0)
- APP_HOST (optional)
- APP_PORT (optional)



## Implementation notes
- Use aioredis or redis.asyncio for async Redis connections
- Prefer background tasks or long-lived coroutines for subscription loops
- Be careful with blocking APIs — always use async-friendly Redis clients
- For production use, handle reconnects, channel management, and backpressure

## Testing
- Unit tests can mock redis and check publisher logic
- Integration tests can run against a test Redis instance (Docker) and verify message flow



## Further reading
- FastAPI docs for background tasks, SSE, and WebSockets
- redis.asyncio / aioredis docs for async Redis usage

This file demonstrates how the FastAPI app integrates with Redis Pub/Sub for simple publish/subscribe communication. Modify examples for your production requirements.