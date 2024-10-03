import asyncpg
from asyncpg import Pool
from typing import Any, List, Optional

class UninitializedDatabasePoolError(Exception):
    def __init__(
        self,
        message="The database connection pool has not been properly initialized.Please ensure setup is called",
    ):
        self.message = message
        super().__init__(self.message)

class DataBasePool:
    _db_pool: Optional[Pool] = None
    @classmethod
    async def setup(cls, timeout: Optional[float] = None):
        """
        Asynchronously sets up a database connection pool with optional timeout.
        Parameters:
            - cls (Type): The class to which the database pool is being added.
            - timeout (Optional[float]): Optional timeout value for the database operations.
        Returns:
            - None: This function does not return a value.
        Example:
            - await setup(MyClass, timeout=30)
        """
        cls._db_pool = await asyncpg.create_pool(
            dsn="postgres://postgres:password@localhost:5433/postgres", 
            min_size=10,
            max_size=30, 
            timeout=60
            )
        cls._timeout = timeout

    @classmethod
    async def get_pool(cls):
        """
        Asynchronously retrieves the database connection pool.
        Parameters:
            - cls (type): The class instance to access the database pool attribute.
        Returns:
            - type: The database connection pool if initialized.
        Example:
            - await get_pool(SomeClass) -> <DatabaseConnectionPool instance>
        """
        if not cls._db_pool:
            raise UninitializedDatabasePoolError()
        return cls._db_pool

    @classmethod
    async def teardown(cls):
        """
        Asynchronously tears down the database pool connection.
        Parameters:
            - cls (type: class object): The class object containing the database pool.
        Returns:
            - None: This function does not return any value.
        Example:
            - await function(MyClass) -> None
        """
        if not cls._db_pool:
            raise UninitializedDatabasePoolError()
        await cls._db_pool.close()

async def execute_query_with_pool(query: str, *args: Any, fetch: bool = False, fetch_one: bool = False) -> Optional[List[Any]]:
    """
    Executes a given SQL query using a connection pool with transaction support.
    Parameters:
        - query (str): The SQL query to be executed.
        - *args (Any): Variable length argument list to be used with the query.
        - fetch (bool): Optional; If True, fetches all rows matching the query. Defaults to False.
        - fetch_one (bool): Optional; If True, fetches a single row matching the query. Defaults to False.
    Returns:
        - Optional[List[Any]]: The result of the executed query. Returns a list of rows, a single row, or an execution result based on the fetch parameters.
    Example:
        - execute_query_with_pool("SELECT * FROM users WHERE id = $1", 1, fetch=True) -> [{"id": 1, "name": "John Doe"}]
    """
    db_pool: Pool = await DataBasePool.get_pool()
    async with db_pool.acquire() as connection:
        async with connection.transaction():
            if fetch:
                result = await connection.fetch(query, *args)
            elif fetch_one:
                result = await connection.fetchrow(query, *args)
            else:
                result = await connection.execute(query, *args)
            return result   

async def execute_query(query: str, *args: Any, fetch: bool = False, fetch_one: bool = False) -> Optional[List[Any]]:
    """
    Executes a SQL query asynchronously using asyncpg and returns the result based on the fetch options.
    Parameters:
        - query (str): The SQL query to execute.
        - *args (Any): Variable length argument list to pass parameters to the SQL query.
        - fetch (bool, optional): Whether to fetch multiple rows from the query (default is False).
        - fetch_one (bool, optional): Whether to fetch a single row from the query (default is False).
    Returns:
        - Optional[List[Any]]: The query result based on the fetch options, or None if an error occurs.
    Example:
        - execute_query("SELECT * FROM users WHERE id=$1", 1, fetch=True) -> [{'id': 1, 'name': 'John Doe'}]
    """
    conn = await asyncpg.connect(
        database="postgres", user="postgres", password="password", host="localhost", port=5433
    )
    try:
        if fetch:
            result = await conn.fetch(query, *args)
        elif fetch_one:
            result = await conn.fetchrow(query, *args)
        else:
            result = await conn.execute(query, *args)
    except (asyncpg.PostgresError, ConnectionResetError) as e:
        print(f"Database error: {e}")
    finally:
        await conn.close()

    return result