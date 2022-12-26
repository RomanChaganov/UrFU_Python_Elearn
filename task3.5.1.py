import sqlite3

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
