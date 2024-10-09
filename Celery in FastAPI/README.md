# Celery in FastAPI
This repository demonstrates how to integrate Celery with FastAPI to handle background tasks effectively. It provides a practical example of task queues, how to offload time-consuming operations to background workers using Celery, and why Celery can be a better fit for certain use cases than FastAPI's built-in background tasks.

## Features

* FastAPI: A modern web framework for building APIs with Python 3.7+ based on standard Python type hints.
* Celery: An asynchronous task queue/job queue system that is widely used for real-time operations.
* RabbitMQ: A message broker that Celery uses to send and receive messages between workers and the web app.


## Why Use Celery?
While FastAPI provides a built-in background task feature, Celery is more suited for complex use cases such as:

* Running long-running tasks asynchronously
* Scheduling periodic tasks
* Retrying failed tasks
* Running tasks distributed across multiple worker nodes

## Conclusion

This project demonstrates how to integrate Celery with FastAPI to handle background tasks more effectively. With the help of RabbitMQ as a message broker, we can distribute and manage tasks in a scalable and reliable manner.