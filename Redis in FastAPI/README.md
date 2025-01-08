## Redis in FastAPI

This project demonstrates how to integrate Redis with FastAPI to leverage caching and session management capabilities. Redis is an in-memory data structure store that can be used as a database, cache, and message broker. By integrating Redis with FastAPI, you can improve the performance and scalability of your applications by caching responses, managing sessions, and storing temporary data efficiently.

## Features

- Caching API responses using Redis
- Deleting cached keys with a specific suffix
- Simulating delays to demonstrate caching benefits

## Requirements

- Python 3.7+
- FastAPI
- Redis
- `redis-py` library

## Installation

1. Install the required dependencies:
    ```bash
    pip install fastapi uvicorn redis
    ```

2. Ensure you have Redis installed and running on your local machine. You can start Redis using the following command:
    ```bash
    redis-server
    ```

## Running the Application

1. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

2. The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

### POST /get_details

This endpoint simulates a delay (e.g., for a database query) and returns the provided data. The response is cached using Redis.

- **Request Body**: JSON object containing the data to be processed.
- **Response**: JSON object containing the processed data.

Example:
```bash
curl -X POST "http://127.0.0.1:8000/get_details" -H "Content-Type: application/json" -d '{"key": "value"}'
