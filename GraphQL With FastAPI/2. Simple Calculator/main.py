from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry
import typing

@strawberry.type
class Calculate:
    @strawberry.field
    def add(self, a: float, b: float) -> float:
        return a + b

    @strawberry.field
    def subtract(self, a: float, b: float) -> float:
        return a - b

    @strawberry.field
    def multiply(self, a: float, b: float) -> float:
        return a * b

    @strawberry.field
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

schema = strawberry.Schema(query=Calculate)
graphql_app = GraphQLRouter(schema)
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")