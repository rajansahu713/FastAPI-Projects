# FastAPI PostgreSQL Docker Application

This project demonstrates setting up a FastAPI application with a PostgreSQL database, all containerized using Docker.

## Prerequisites
Ensure you have the following installed:
* Python 3.11
Docker
* Docker Compose

## Setup Instructions
Clone the repository and navigate to the project directory.

Ensure you have the following structure:

```
fastapi-postgres-docker/
|-- main.py
|-- databases.py
│-- models.py
│-- schemas.py
│-- Dockerfile
│-- requirements.txt
└── docker-compose.yml
```

Build and start the application using Docker Compose:

```
docker-compose up --build
```
Access the FastAPI application at http://localhost:8000.

### Files Overview
* databases.py: Database configuration and setup.
* Dockerfile: Docker configuration for the FastAPI application.
* docker-compose.yml: Docker Compose configuration to run both FastAPI and PostgreSQL.

### API Endpoints
* POST /items/: Create a new item.
* GET /items/{item_id}: Read an item by ID.
* PUT /items/{item_id}: Update an item by ID.
* DELETE /items/{item_id}: Delete an item by ID.

By following these steps, you will have a FastAPI application with a PostgreSQL database running in Docker containers.