#!/usr/bin/env python3
"""Database variable checking functions"""
import sys
from dateutil.parser import parse


def number_checker(price):
    try:
        price = int(price)
        return price
    except ValueError:
        sys.exit(">>> Not a number.")

def category_checker(cat, cats):
    if cat.title() not in cats:
        sys.exit(">>> Not a category.")
    else:
        return cat.lower()

def date_checker(date):
    try:
        check = parse(date, yearfirst=True)
        return str(check).split()[0]
    except Exception as e:
        sys.exit(e)

def month_checker(month):
    month = number_checker(month)
    if not 0 < month < 13:
        sys.exit(">>> A month is between 1 and 12.")
    else:
        return month

def category_name_checker(name, cats):
    if name in [i.name for i in cats]:
        sys.exit(f">>> {name.title()} already exists in your category list.")

def cc_checker(cc):
    if cc == "cc":
        return True
    elif cc == "c":
        return False
    else:
        sys.exit(">>> {cc} is invalid, 'c' for cash, 'cc' for credit.")

def arg_len_checker(args, amt):
    if len(args) > amt:
        sys.exit(f">>> This command doesn't take more than {amt} arguments.'")
