#!/usr/bin/env python3
from utils.models import DB
from utils.models import Item
from utils.models import Category

def create_db():
    DB.connect()
    DB.create_tables([Item, Category])
    print(">>> Created database for budget entries, ready to use.")

if __name__ == "__main__":
    create_db()
