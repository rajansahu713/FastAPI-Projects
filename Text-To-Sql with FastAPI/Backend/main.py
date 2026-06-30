from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from text_to_sql import text_to_sql

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/status")
def read_root():
    return {"Message": "Server is Running Successfully"}


@app.post("/api/v1/chat")
def chat(body: dict):
    data = text_to_sql(body.get("question"))
    return {"data": data}