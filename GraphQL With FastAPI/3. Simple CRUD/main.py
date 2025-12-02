import strawberry
from typing import Optional, List

@strawberry.type
class User:
    id: int
    name: str
    email: str


@strawberry.input
class UserInput:
    name: str
    email: str

@strawberry.input
class UserUpdateInput:
    id: int
    name: Optional[str] = None
    email: Optional[str] = None



fake_db = [
    {"id": 1, "name": "Rajan", "email": "rajan@example.com"},
    {"id": 2, "name": "Amit", "email": "amit@example.com"},
]

@strawberry.type
class Query:

    @strawberry.field
    def users(self) -> List[User]:
        return [User(**u) for u in fake_db]

    @strawberry.field
    def user_by_id(self, id: int) -> Optional[User]:
        for u in fake_db:
            if u["id"] == id:
                return User(**u)
        return None


@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_user(self, data: UserInput) -> User:
        new_id = len(fake_db) + 1
        user = {"id": new_id, "name": data.name, "email": data.email}
        fake_db.append(user)
        return User(**user)

    @strawberry.mutation
    def update_user(self, data: UserUpdateInput) -> Optional[User]:
        for user in fake_db:
            if user["id"] == data.id:
                if data.name:
                    user["name"] = data.name
                if data.email:
                    user["email"] = data.email
                return User(**user)
        return None

    @strawberry.mutation
    def delete_user(self, id: int) -> bool:
        global fake_db
        for user in fake_db:
            if user["id"] == id:
                fake_db = [u for u in fake_db if u["id"] != id]
                return True
        return False


schema = strawberry.Schema(query=Query, mutation=Mutation)

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
