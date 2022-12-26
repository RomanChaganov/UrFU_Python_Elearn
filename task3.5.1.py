import sqlite3
import pandas as pd

# df = pd.read_csv('Currency_data.csv')
with sqlite3.connect('database.db') as db:
    # df.to_sql(name='currency', con=db)
    cursor = db.cursor()
    print(cursor.fetchone())