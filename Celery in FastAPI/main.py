# main.py
from fastapi import FastAPI
from celery.result import AsyncResult
from celery_main import send_email_task

app = FastAPI()
@app.post("/send-email/")
async def send_email(email: str, subject: str, body: str):
    # Asynchronously send an email using Celery
    task = send_email_task.delay(email, subject, body)
    return {"task_id": task.id}

@app.get("/task-status/{task_id}")
async def get_task_status(task_id: str):
    # Check the status of the Celery task
    task_result = AsyncResult(task_id)
    return {"task_id": task_id, "status": task_result.status, "result": task_result.result}