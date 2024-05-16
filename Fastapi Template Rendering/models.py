from pydantic import BaseModel

class ToDoItem(BaseModel):
    title: str
    description: str
    completed: bool = False
