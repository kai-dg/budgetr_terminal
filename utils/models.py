#!/usr/bin/env python3
"""All database models.
TODO
subtracting feature:
add to notes (add newline if not empty), 'sub: item notes'
"""
from peewee import *
DB = SqliteDatabase('data.db')


class BaseModel(Model):
    class Meta:
        database = DB

class Category(BaseModel):
    name = CharField(max_length=30, unique=True)
    notes = TextField()

class Item(BaseModel):
    date = DateField()
    price = IntegerField()
    notes = TextField()
    category = CharField(max_length=30)
    cc = BooleanField(default=True)

if __name__ == "__main__":
    pass
