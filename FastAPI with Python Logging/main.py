from fastapi import FastAPI
from logger_setup import logger


# Create FastAPI app
app = FastAPI()

# Example FastAPI route
@app.get("/")
async def read_root():
    # Example logging for different levels
    logger.info("Info log message")
    logger.warning("Warning log message")
    logger.error("Error log message")
    return {"message": "Hello World"}
