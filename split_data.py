"""
Данный скрипт разделяет исходный файл данных на файлы, разделенные по году
"""

import pandas as pd
from report_out_old import formatter_date


class SplitData:
    def __init__(self, file_name):
        pd.set_option('expand_frame_repr', False)
        df = pd.read_csv(file_name)
        df['years'] = df['published_at'].apply(formatter_date)
        years = df['years'].unique()

        for year in years:
            data = df[df['years'] == year]
            data.drop(columns='years').to_csv(rf'csv_files\part_{year}.csv', index=False)

SplitData('vacancies_by_year.csv')