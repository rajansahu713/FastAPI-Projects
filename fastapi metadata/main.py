from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

class UnderMaintenanceException(HTTPException):
    def __init__(self, detail="Service is under maintenance"):
        super().__init__(status_code=503, detail=detail)

    def __str__(self):
        return f"{self.detail}"

def check_maintenance():
    if 1 == 2:  # Change this condition to actually check maintenance status
        raise UnderMaintenanceException

app = FastAPI(
    title="FastAPI Template",
    description="A template for FastAPI",
    version="0.1.0",
    docs_url="/docs",
    redoc_url=None,
    dependencies=[Depends(check_maintenance)]
)

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "PUT", "DELETE", "OPTIONS"],  # Restricting to specific methods
    allow_headers=['*'],
)

@app.exception_handler(UnderMaintenanceException)
async def maintenance_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.get("/r")
def read_root():
    return {"Hello": "World"}
