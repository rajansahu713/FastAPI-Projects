import strawberry
from typing import List, Optional
from sqlalchemy.future import select
from models import Book
from db import AsyncSessionLocal


@strawberry.type
class BookType:
    id: int
    title: str
    author: str


@strawberry.type
class Query:

    @strawberry.field
    async def books(self) -> List[BookType]:
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(Book))
            books = result.scalars().all()
            return [BookType(id=b.id, title=b.title, author=b.author) for b in books]

    @strawberry.field
    async def book(self, id: int) -> Optional[BookType]:
        async with AsyncSessionLocal() as session:
            book = await session.get(Book, id)
            if not book:
                return None
            return BookType(id=book.id, title=book.title, author=book.author)


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def create_book(self, title: str, author: str) -> BookType:
        async with AsyncSessionLocal() as session:
            new_book = Book(title=title, author=author)
            session.add(new_book)
            await session.commit()
            await session.refresh(new_book)
            return BookType(id=new_book.id, title=new_book.title, author=new_book.author)

    @strawberry.mutation
    async def update_book(self, id: int, title: str, author: str) -> Optional[BookType]:
        async with AsyncSessionLocal() as session:
            book = await session.get(Book, id)
            if not book:
                return None
            book.title = title
            book.author = author
            await session.commit()
            await session.refresh(book)
            return BookType(id=book.id, title=book.title, author=book.author)

    @strawberry.mutation
    async def delete_book(self, id: int) -> bool:
        async with AsyncSessionLocal() as session:
            book = await session.get(Book, id)
            if not book:
                return False
            await session.delete(book)
            await session.commit()
            return True


schema = strawberry.Schema(Query, Mutation)
