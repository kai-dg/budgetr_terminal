# Budgetr - Terminal
Very basic budget tracker for people that like to use the terminal

## Setup
Run `setup.py`
Run `pip install -r requirements.txt`

## Commands
**Updating stuff**
- `add`: Adds a budget entry
- `update`: Updates a budget entry
- `delete`: Deletes a budget entry
- `addcat`: Adds a category name
- `updatecat`: Updates a category name
- `deletecat`: Deletes a category name

**Displaying stuff**
### [] = optional

- `month [MONTH#]`: Displays entries for current month by default, or target month if entered

## TODO
- Distinguish between credit and cash
- Flexible and simple command to display entries and stats
- Import and export from CSV

## Editing Notes
Function order: models.py -> model_funcs.py -> argfuncs.py -> argparser.py

## Author
[kai-dg](https://github.com/kai-dg)
