import sqlite3
import pandas as pd
import numpy as np
import math

"""
Функциональность модуля заключается в формировании данных о вакансий и их сохранение в БД
"""

def none_to_nan(num):
    """
    Функция превращает None в NAN
    Args:
        num (float or None): изначальное число

    Returns:
        (float): Либо Nan, либо число
    """
    if num is None:
        return np.NAN
    else:
        return num

def to_int(num):
    """
    Функция превращает Nan в None или берет целую часть от числа
    Args:
        num(Nan or float):

    Returns:
        (None or int): Либо None, либо целое число
    """
    if math.isnan(num):
        return None
    else:
        return int(num)

df = pd.read_csv('vacancies_dif_currencies.csv')
print('Файл вакансий загружен')
df.salary_from = df[['salary_from', 'salary_to']].mean(axis=1)
df['published_at'] = df.published_at.apply(lambda z: z[:7])
currency_to_num = {
    'BYR': 2, 'EUR': 3, 'KZT': 4, 'UAH': 5, 'USD': 6, 'UZS': 7, 'KGS': 8, 'AZN': 9, 'GEL': 10
}

with sqlite3.connect('Chaganov.db') as con:
    print('База данных загружена')
    cursor = con.cursor()
    cursor.execute('DROP TABLE IF EXISTS salary')
    cursor.execute('''CREATE TABLE salary (
        name TEXT,
        salary INTEGER,
        area_name TEXT,
        published_at TEXT
        )''')
    df['salary_from'] = df.apply(
        lambda x: to_int(float(x['salary_from'] * none_to_nan(cursor.execute(f'SELECT * FROM currency WHERE date = "{x["published_at"]}"').fetchone()[currency_to_num[x['salary_currency']]])))
        if (x['salary_currency'] != 'RUR' and not np.isnan(x['salary_from']))
        else x['salary_from'], axis=1
    )
    df = df.drop(['salary_to', 'salary_currency'], axis=1).rename(columns={'salary_from': 'salary'})
    df.to_sql(name='salary', con=con, if_exists='append', index=False, index_label=False)

    # cursor.execute('ALTER TABLE salary ADD COLUMN salary INTEGER')
    # cursor.execute('UPDATE salary SET salary = CAST(salary_from as INTEGER)')
    # cursor.execute('ALTER TABLE salary DROP COLUMN salary_from')