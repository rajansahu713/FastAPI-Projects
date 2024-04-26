# crud.py

from sqlalchemy.orm import Session, Query
from models import Item
from sqlalchemy import func, desc
from math import ceil
from models import Item


def pagination(query: Query, current_page: int = 1, records_per_page: int = 10):
    # Calculate the offset based on the current page and records per page
    offset = (current_page - 1) * records_per_page

    # Query total number of records
    total_records = query.session.query(func.count()).select_from(query.subquery()).scalar()

    # Calculate the last page number
    last_page = ceil(total_records / records_per_page)

    # Query items using the calculated offset and records per page
    items = query.offset(offset).limit(records_per_page).all()

    return {
        "current_page": current_page,
        "last_page": last_page,
        "total_records": total_records,
        "items": items
    }


def get_items(db: Session, current_page: int = 1, records_per_page: int = 10):
    query = db.query(Item).order_by(desc(Item.id))
    result = pagination(query, current_page=current_page, records_per_page=records_per_page)
    return result

def create_item(db: Session, item: Item):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted"}