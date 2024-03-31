from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str]


class ItemCreate(BaseModel):
    name: str
    description: Optional[str]


class ItemUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]