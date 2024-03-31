from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from .schemas import ItemCreate, Item, ItemUpdate
from .databases import SessionLocal, engine
from .models import DBItem, Base

app = FastAPI()

# Dependency to get the database session
def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return "server is running"


@app.post("/items")
def create_item(item: ItemCreate, db: Session = Depends(get_db)) -> Item:
    db_item = DBItem(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return Item(**db_item.__dict__)


@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)) -> Item:
    db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(**db_item.__dict__)


@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)) -> Item:
    db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.model_dump().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return Item(**db_item.__dict__)


@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)) -> Item:
    db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return Item(**db_item.__dict__)