#!/usr/bin/env python3
"""Functions that add, delete, update to database.
Notes:
    Input classes should handle all modification parameters (add, delete, update).
    Controller classes control the database models.
    Controller can be a standalone class, just feed it `data`.
"""
import utils.checks as c
import datetime
import calendar
from utils.models import Item
from utils.models import Category
CURR = datetime.date.today()
CURR_YEAR = CURR.year
CURR_MONTH = CURR.month


def list_categories() -> list:
    """Used when adding or modifying entries to show what is available"""
    cats_db = Category.select()
    cats = [c.name.title() for c in cats_db]
    print(f"** Available: {' '.join(cats)} **")
    return cats

class ItemInput:
    def __init__(self):
        self.date = str(CURR)
        self.category = None
        self.price = None
        self.notes = ""
        self.cc = True
        self.idx = None
        self.month = CURR_MONTH

    def add(self):
        date = input("Date (Y-M-D): ")
        if date != "":
            self.date = c.date_checker(date)
        cats = list_categories()
        self.category = c.category_checker(input("Category: "), cats)
        self.price = c.number_checker(input("Price: "))
        self.cc = c.cc_checker(input("Credit 'cc' or Cash 'c': "))
        self.notes = input("Notes: ")

    def update(self):
        month = input("> Which month? (Leave blank for current month): ")
        if month != "":
            self.month = c.month_checker(month)
        self.idx = c.number_checker(input("> Which ID? "))
        print("(Leave blank to skip)")
        self.date = input("Date (Y-M-D): ")
        if self.date != "":
            self.date = c.date_checker(self.date)
        cats = list_categories()
        self.category = input("Category: ")
        if self.category != "":
            self.category = c.category_checker(self.category, cats)
        self.price = input("Price: ")
        if self.price != "":
            self.price = c.number_checker(self.price)
        self.cc = input("Cash 'c' or Credit 'cc': ").lower()
        if self.cc != "":
            self.cc = c.cc_checker(self.cc)
        self.notes = input("Notes: ")
        if self.notes != "":
            self.notes = self.notes

    def delete(self):
        month = input("> Which month? (Leave blank for current month): ")
        if month != "":
            self.month = c.month_checker(month)
        self.idx = c.number_checker(input("Deleting Item ID: "))

class ItemController:
    def add(self, data):
        i = Item.create(
            date = data['date'],
            price = data['price'],
            category = data['category'],
            cc = data['cc'],
            notes = data['notes']
        )
        i.save()

    def update(self, data):
        q = Item.select().where(Item.date.month==data["m"], Item.date.year==CURR_YEAR)
        idx = q[data["id"]]
        if data["date"] != "":
            print(f"Updated {q[data['id']].date} to {data['date']}")
            q = (Item.update({Item.date:data["date"]}).where(Item.id==idx))
            q.execute()
        if data["category"] != "":
            print(f"Updated {q[data['id']].category} to {data['category']}")
            q = (Item.update({Item.category:data["category"]}).where(Item.id==idx))
            q.execute()
        if data["price"] != "":
            print(f"Updated {q[data['id']].price} to {data['price']}")
            q = (Item.update({Item.price:data["price"]}).where(Item.id==idx))
            q.execute()
        if data["cc"] != "":
            print(f"Updated payment type for entry dated {q[data['id']].date}")
            q = (Item.update({Item.cc:data["cc"]}).where(Item.id==idx))
            q.execute()
        if data["notes"] != "":
            print(f"Updated {q[data['id']].notes} to {data['notes']}")
            q = (Item.update({Item.notes:data["notes"]}).where(Item.id==idx))
            q.execute()

    def delete(self, data):
        q = Item.select().where(Item.date.month==data["m"], Item.date.year==CURR_YEAR)
        itemid = q[data["id"]]
        print(f">>> Deleted budget entry dated {q[data['id']].date}")
        d = (Item.delete().where(Item.id == itemid))
        d.execute()

class CategoryInput:
    def __init__(self):
        self.name = ""
        self.notes = ""
        self.idx = ""

    def add(self):
        self.name = input("New Category Name: ").lower()
        self.notes = input("Description: ")

    def update(self):
        cats = list_categories()
        self.idx = c.category_checker(input("Enter category name to modify: "), cats)
        print("(Leave blank to skip)")
        self.name = input("New Category Name: ").lower()
        self.notes = input("Description: ")

    def delete(self):
        cats = list_categories()
        self.idx = c.category_checker(input("Enter category name to delete: "), cats)

class CategoryController:
    def add(self, data):
        cats = Category.select()
        c.category_name_checker(data['name'], cats)
        cat = Category.create(
            name = data['name'],
            notes = data['notes']
        )
        cat.save()
        print(f">>> Added new category named {data['name'].title()}")

    def update(self, data):
        if data["notes"] != "":
            print(f"Updated {data['id']} notes to {data['notes']}")
            q = (Category.update({Category.name:data["name"]}).where(Category.name==data["id"]))
            q.execute()
        if data["name"] != "":
            print(f"Updated {data['id']} to {data['name']}")
            q = (Category.update({Category.name:data["name"]}).where(Category.name==data["id"]))
            q.execute()

    def delete(self, data):
        d = (Category.delete().where(Category.name == data["id"]))
        d.execute()

class Display:
    """Init -> Query DB -> Create stats tempalte.
    Itemizing list tracks each category expense.
    """
    def __init__(self, month=CURR_MONTH, year=CURR_YEAR):
        self.month = month
        self.year = year
        self.query = self.date_query()
        self.stats = self.stats_template()
        self.day_amt = calendar.monthrange(self.year, self.month)[1]
        self.cc_tag = " - CC"
        self.no_cc_tag = "     " # balancing out terminal print with cc_tag

    def stats_template(self) -> dict:
        cats_db = Category.select()
        data = {
            "cats": {ca.name.title():0 for ca in cats_db},
            "expense": 0
        }
        return data

    def date_query(self):
        """TODO:
            sort_by option
            week query?
        """
        q = Item.select().where(Item.date.month==self.month, Item.date.year==self.year).order_by(Item.date)
        return q

    def itemized_list(self):
        idx = 0
        print("ID\tDate\t\tCategory\tPrice\tNotes")
        for i in self.query:
            category = i.category.title() + self.no_cc_tag
            if i.cc == True:
                category = category.rstrip() + self.cc_tag
            self.stats["expense"] += i.price
            self.stats["cats"][i.category.title()] += i.price
            print(f"{idx}\t{i.date}\t{category}\t{i.price}\t{i.notes}")
            idx += 1
        print()

    def category_stats(self):
        for i in self.stats["cats"]:
            amt = self.stats["cats"][i]
            if amt != 0:
                print(f"* {i} Usage: {amt} | {(amt/self.stats['expense'])*100:.1f}%")

    def total_stats(self):
        expense = self.stats["expense"]
        print(f"\n** Total Usage: {expense}")
        print(f"** Daily Usage: {int(expense/self.day_amt)}\n")

if __name__ == "__main__":
    pass
