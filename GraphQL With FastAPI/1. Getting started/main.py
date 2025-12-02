from typing import Optional
import uvicorn
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Query:
    @strawberry.field
    def hello(self, name: Optional[str] = None) -> str:
        if name:
            return f"Hello, {name}! Welcome to FastAPI and GraphQL!"
        return "Welcome to FastAPI and GraphQL!"


schema = strawberry.Schema(query=Query)

app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
