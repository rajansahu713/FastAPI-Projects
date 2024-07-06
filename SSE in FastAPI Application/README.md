# Server-Sent Events in FastAPI Application

This project demonstrates a live sports scores application using FastAPI and Server-Sent Events (SSE). The server sends live score updates to the client, which displays them in real-time. The updates are sourced from a JSON file.

## Features
* FastAPI-based backend for serving live score updates.
* Server-Sent Events (SSE) for real-time data streaming.
* Simple frontend to display live football scores.
* Cross-Origin Resource Sharing (CORS) enabled for client-server interaction.

## Project Structure
```bash
.
├── app.py          # Main FastAPI application
├── scores.json     # JSON file with the match scores data
├── index.html      # Frontend HTML to display the live scores
├── README.md       # Project documentation
```
## Getting Started

### Prerequisites
* Python 3.8+
* FastAPI
* sse-starlette
* Uvicorn (for running the FastAPI application)

## Browser View
```
Live Football Scores
Match Summary: {"time": "00:01", "scores": "1:0", "event": "Goal! Team A scores!"}
Match Summary: {"time": "00:05", "scores": "1:1", "event": "Goal! Team B scores!"}
Match Summary: {"time": "00:10", "scores": "2:1", "event": "Goal! Team A scores again!"}
```