# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from pydantic import BaseModel
import crud

app = FastAPI()



# Dependency to get a session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define an endpoint to get paginated items using cursor-based pagination
@app.get("/items/")
async def get_items(current_page: int = 0, records_per_page: int = 10, db: Session = Depends(get_db)):
    items = crud.get_items(db, current_page=current_page, records_per_page=records_per_page)
    return items


class ItemCreate(BaseModel):
    name: str
    description: str

@app.post("/items/")
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    crud.create_item(db, item)
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    crud.delete_item(db, item_id)
    return {"message": "Item deleted"}

