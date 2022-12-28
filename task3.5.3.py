import sqlite3
import pandas as pd

""" Модуль посредством sql запросов получает статистику по вакансиям"""

job_name = input('Введите название вакансии: ')

with sqlite3.connect('Chaganov.db') as con:
    pd.set_option('expand_frame_repr', False)
    salary_by_year = pd.read_sql("""
        SELECT strftime('%Y', published_at) as date, round(avg(salary)) as salary_by_year
        FROM salary
        GROUP BY strftime('%Y', published_at)""", con)
    vacs_by_years = pd.read_sql("""
        SELECT strftime('%Y', published_at) as date, count(salary) as vacs_by_years
        FROM salary
        GROUP BY strftime('%Y', published_at)""", con)
    job_salary_by_years = pd.read_sql(f"""
        SELECT strftime('%Y', published_at) as date, round(avg(salary)) as job_salary_by_years
        FROM salary
        WHERE name LIKE '{job_name}'
        GROUP BY strftime('%Y', published_at)""", con)
    job_count_by_years = pd.read_sql(f"""
        SELECT strftime('%Y', published_at) as date, count(salary) as job_count_by_years
        FROM salary
        WHERE name LIKE '{job_name}'
        GROUP BY strftime('%Y', published_at)""", con)
    salary_by_cities = pd.read_sql("""
        SELECT area_name as city, count(salary) as vacs_by_cities, round(avg(salary)) as salary_by_cities
        FROM salary
        GROUP BY area_name
        ORDER BY vacs_by_cities DESC
        LIMIT 10""", con)
    salary_by_cities = salary_by_cities.drop('vacs_by_cities', axis=1)
    vacs_by_cities = pd.read_sql("""
        SELECT area_name as city, count(salary) as vacs_by_cities
        FROM salary
        GROUP BY area_name
        ORDER BY vacs_by_cities DESC
        LIMIT 10""", con)

    print(salary_by_year.to_string() + '\n')
    print(vacs_by_years.to_string() + '\n')
    print(job_salary_by_years.to_string() + '\n')
    print(job_count_by_years.to_string() + '\n')
    print(salary_by_cities.to_string() + '\n')
    print(vacs_by_cities.to_string() + '\n')
