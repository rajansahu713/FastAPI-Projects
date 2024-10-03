import asyncpg
from fastapi import Depends, FastAPI
from database import DataBasePool, execute_query_with_pool, execute_query
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handle the lifespan of the FastAPI application for resource setup and teardown.
    Parameters:
        - app (FastAPI): The FastAPI application instance.
    Returns:
        - None: This function does not return anything.
    Example:
        - No direct usage example as this function is used internally by FastAPI.
    """
    await DataBasePool.setup()  # Initialize pool
    try:
        yield
    finally:
        await DataBasePool.teardown() 

app = FastAPI(lifespan=lifespan)

@app.get("/with_pool")
async def handle(db_pool:asyncpg.Pool = Depends(DataBasePool.get_pool)):
    """
    Asynchronously handles a database transaction to fetch the count of employees.
    Parameters:
        - db_pool (asyncpg.Pool): Database connection pool, provided by dependency injection with a default of DataBasePool.get_pool.
    Returns:
        - dict: A dictionary containing the count of employees with the key 'result'.
    Example:
        - handle(db_pool) -> {'result': 150}
    """

    async with db_pool.acquire() as connection:
        async with connection.transaction():
            query = "SELECT * FROM employee_information limit 10"
            result = await execute_query_with_pool(query, fetch=True)
            return {"result": result}

@app.get("/without_pool")
async def without_pool():
    """
    Execute a SQL query to count records in the employee_information table without using a connection pool.
    Parameters:
        None
    Returns:
        - dict: A dictionary containing the count of records in the employee_information table.
    Example:
        - without_pool() -> {"result": 42}
    """
    query = "SELECT COUNT(*) FROM employee_information"
    data = await execute_query(query, fetch_one=True)
    return {"result": data}