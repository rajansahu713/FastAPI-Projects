from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.memory import MemoryJobStore
import os

# Create a FastAPI app instance
app = FastAPI()

# Initialize a SQLAlchemyJobStore with SQLite database
jobstores = {
    'default': MemoryJobStore()
}

# Initialize an AsyncIOScheduler with the jobstore
scheduler = AsyncIOScheduler(jobstores=jobstores, timezone='Asia/Kolkata') 


# This is a scheduled job that will run every 10 seconds.
@scheduler.scheduled_job('interval', seconds=10)
def scheduled_job_1():
    print("scheduled_job_1")

@scheduler.scheduled_job('date',  run_date='2024-07-21 11:00:00' )
def scheduled_job_2():
    print("scheduled_job_2")

@scheduler.scheduled_job('cron', day_of_week='mon-sun', hour=23, minute=44, second=0)  # Decorator for scheduling the job
def scheduled_job_3():  # Function to be executed at the scheduled time
    print("scheduled_job_3")  

# Register an event for application startup
@app.on_event("startup")
async def startup_event():
    scheduler.start()

@app.on_event("shutdown")
async def shutdown_event():
    scheduler.shutdown()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}