#!/usr/bin/env python3
"""All functions linked to the dictionary in argparser.
Cannot use classes for more than 1 func.
"""
from utils.model_funcs import ItemInput
from utils.model_funcs import ItemController
from utils.model_funcs import CategoryInput
from utils.model_funcs import CategoryController
from utils.model_funcs import Display
ITEM_INPUT = ItemInput()
ITEM_CTRL = ItemController()
CAT_INPUT = CategoryInput()
CAT_CTRL = CategoryController()


def add_item():
    ITEM_INPUT.add()
    data = {
        "date": ITEM_INPUT.date,
        "price": ITEM_INPUT.price,
        "category": ITEM_INPUT.category,
        "cc": ITEM_INPUT.cc,
        "notes": ITEM_INPUT.notes
    }
    ITEM_CTRL.add(data)
    print(f">>> Added new budget entry dated {data['date']}")

def update_item():
    ITEM_INPUT.update()
    data = {
        "m": ITEM_INPUT.month,
        "id": ITEM_INPUT.idx,
        "date": ITEM_INPUT.date,
        "category": ITEM_INPUT.category,
        "cc": ITEM_INPUT.cc,
        "notes": ITEM_INPUT.notes,
        "price": ITEM_INPUT.price
    }
    ITEM_CTRL.update(data)

def delete_item():
    ITEM_INPUT.delete()
    data = {
        "m": ITEM_INPUT.month,
        "id": ITEM_INPUT.idx
    }
    ITEM_CTRL.delete(data)

def add_category():
    CAT_INPUT.add()
    data = {
        "name": CAT_INPUT.name,
        "notes": CAT_INPUT.notes
    }
    CAT_CTRL.add(data)

def update_category():
    CAT_INPUT.update()
    data = {
        "id": CAT_INPUT.idx,
        "name": CAT_INPUT.name,
        "notes": CAT_INPUT.notes
    }
    CAT_CTRL.update(data)

def delete_category():
    CAT_INPUT.delete()
    data = {
        "id": CAT_INPUT.idx
    }
    CAT_CTRL.delete(data)
    print(f">>> Deleted category named {data['id']}")

def display_month(args=[]):
    if len(args) > 0:
        c.arg_len_checker(args, 1)
        d = Display(month=args[0])
    else:
        d = Display()
    d.itemized_list()
    d.category_stats()
    d.total_stats()

if __name__ == "__main__":
    pass
