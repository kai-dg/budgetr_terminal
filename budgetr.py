#!/usr/bin/env python3
import sys
from utils.models import DB
from utils.argparser import argparse
import utils.model_funcs


def main():
    DB.connect()
    args = sys.argv[1:]
    argparse(args)

if __name__ == "__main__":
    main()
    #utils.model_funcs.update_category_input()
