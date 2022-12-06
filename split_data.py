"""
Данный скрипт разделяет исходный файл данных на файлы, разделенные по году
"""

import pandas as pd
from report_out import formatter_date

pd.set_option('expand_frame_repr', False)

file = 'vacancies_by_year.csv'
df = pd.read_csv(file)

df['years'] = df['published_at'].apply(formatter_date)
years = df['years'].unique()

for year in years:
    data = df[df['years'] == year]
    data.drop(columns='years').to_csv(rf'csv_files\part_{year}.csv', index=False)
