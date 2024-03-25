from fastapi import Request
import time

class MyMiddleware:
    def __init__(
            self,
            some_attribute: str,
    ):
        self.some_attribute = some_attribute

    async def __call__(self, request: Request, call_next):
        print("I'm a middleware!")
        start_time = time.time()            
        response = await call_next(request)
        end_time = time.time()

        print("execution time: {} seconds".format(end_time - start_time))
        return response
    

    