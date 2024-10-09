# celery_main.py
from celery import Celery

# Celery configuration with RabbitMQ as the broker
celery_app = Celery(
    "celery_main",
    broker="amqp://guest:guest@localhost:5672//",  
    backend="rpc://"  
)

celery_app.conf.update(
    result_expires=3600,  # Results expire in one hour
)

@celery_app.task
def send_email_task(email: str, subject: str, body: str):
    import time
    time.sleep(5)
    print(f"Email sent to {email} with subject {subject}")
    return {"email": email, "subject": subject, "status": "sent"}