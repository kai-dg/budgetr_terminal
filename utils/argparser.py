#!/usr/bin/env python3
import utils.argfuncs as f
from utils.helper import print_helps
COMMANDS = {
    "add": f.add_item,
    "delete": f.delete_item,
    "update": f.update_item,
    "addcat": f.add_category,
    "deletecat": f.delete_category,
    "updatecat": f.update_category,
    "month": f.display_month
}
HELPS = {
    "help": 0,
    "-help": 0,
    "-h": 0,
    "h": 0
}


def argparse(args:list):
    if len(args) > 1:
        COMMANDS[args[0]](args[1:])
    elif len(args) == 1 and COMMANDS.get(args[0], "") != "":
        COMMANDS[args[0]]()
    elif HELPS.get(args[0], "") != "":
        print_helps()
    else:
        print("Please enter a valid argument.")

if __name__ == "__main__":
    pass
