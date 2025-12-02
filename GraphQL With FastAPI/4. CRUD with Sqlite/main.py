from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from db import engine, Base
from schema import schema

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")