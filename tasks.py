from celery_worker import celery_app
from db import SessionLocal
from models import Item
import random

@celery_app.task
def insert_random_item():
    db = SessionLocal()
    try:
        random_number = random.randint(1, 100)
        name = f"random item {random_number}"
        description = f"random generated description of item {random_number}."
        print(description)
        item = Item(name=name, description=description)
        db.add(item)
        db.commit()
        db.refresh(item)
    finally:
        db.close()