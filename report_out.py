import cProfile
import multiprocessing
import os
import time
from pstats import Stats, SortKey

import numpy as np
import pandas as pd
from multiprocessing import Pool


def formatter_date(input_date):
    """
    Функия преобразует дату в нужный формат

    Args:
        input_date (str): Исходная данные

    Returns:
        (str): Дата в нужном формате
    """
    return int(input_date[:4])


def mean_to_number(numb):
    if numb == np.NAN:
        return 0
    else:
        return int(numb)


currency_to_rub = {
    "AZN": 35.68,
    "BYR": 23.91,
    "EUR": 59.90,
    "GEL": 21.74,
    "KGS": 0.76,
    "KZT": 0.13,
    "RUR": 1,
    "UAH": 1.64,
    "USD": 60.66,
    "UZS": 0.0055,
}


# def prepare_data_from_year(file_name, job_name, data_list):
#     df = pd.read_csv(file_name)
#     df['salary_from'] = df['salary_currency'].map(currency_to_rub) * df['salary_from']
#     df['salary_to'] = df['salary_currency'].map(currency_to_rub) * df['salary_to']
#     df['salary'] = df[['salary_from', 'salary_to']].mean(axis=1)
#     year = df['published_at'].values[0]
#
#     data_list.append([year, int(df['salary'].mean()), len(df),
#                       mean_to_number(df[df['name'].str.contains(job_name)]['salary'].mean()),
#                       len(df[df['name'].str.contains(job_name)])])

def new_prepare_data(file_name, job_name):
    df = pd.read_csv(file_name)
    df['salary_from'] = df['salary_currency'].map(currency_to_rub) * df['salary_from']
    df['salary_to'] = df['salary_currency'].map(currency_to_rub) * df['salary_to']
    df['salary'] = df[['salary_from', 'salary_to']].mean(axis=1)
    year = df['published_at'].values[0]

    return [year, int(df['salary'].mean()), len(df),
            mean_to_number(df[df['name'].str.contains(job_name)]['salary'].mean()),
            len(df[df['name'].str.contains(job_name)])]


class InputConnect:
    job_name = None
    file_name = None

    def __init__(self):
        self.start_time = None
        self.salary_by_years = None
        self.vacs_by_years = None
        self.job_salary_by_years = None
        self.job_count_by_years = None

        params = InputConnect.get_params()

        InputConnect.file_name, InputConnect.job_name = params
        pd.set_option('expand_frame_repr', False)
        self.start_time = time.time()
        df = pd.read_csv(self.file_name)
        self.print_data(df, self.start_time)

    @staticmethod
    def get_params():
        """
        Метод получает входные данные

        Returns:
            (str, str): Кортеж входных параметров
        """
        file_name = input('Введите название файла: ')
        vac_name = input('Введите название профессии: ')
        return file_name, vac_name

    @staticmethod
    def split_data(df):
        df['published_at'] = df['published_at'].apply(formatter_date)
        years = df['published_at'].unique()
        for year in years:
            data = df[df['published_at'] == year]
            data.to_csv(rf'csv_files\part_{year}.csv', index=False)

    @staticmethod
    def prepare_data_from_year(file_name):
        df = pd.read_csv(file_name)
        df['salary_from'] = df['salary_currency'].map(currency_to_rub) * df['salary_from']
        df['salary_to'] = df['salary_currency'].map(currency_to_rub) * df['salary_to']
        df['salary'] = df[['salary_from', 'salary_to']].mean(axis=1)
        year = df['published_at'].values[0]

        return [year, int(df['salary'].mean()), len(df),
                mean_to_number(df[df['name'].str.contains(InputConnect.job_name)]['salary'].mean()),
                len(df[df['name'].str.contains(InputConnect.job_name)])]

    def print_data(self, df, startime):
        InputConnect.split_data(df)
        years = df['published_at'].unique()

        salary_by_years = {year: 0 for year in years}
        vacs_by_years = {year: 0 for year in years}
        job_salary_by_years = {year: 0 for year in years}
        job_count_by_years = {year: 0 for year in years}

        params = []
        files = os.listdir('csv_files')
        for file in files:
            params.append((os.path.join('csv_files', file), InputConnect.job_name))
        with Pool() as p:
            multiprocessing.freeze_support()
            result_list = p.starmap(new_prepare_data, params)

        for data in result_list:
            year = data[0]
            salary_by_years[year] = data[1]
            vacs_by_years[year] = data[2]
            job_salary_by_years[year] = data[3]
            job_count_by_years[year] = data[4]

        # data_list = []
        # files = os.listdir('csv_files')
        # for file in files:
        #     # prepare_data_from_year(os.path.join('csv_files', file), InputConnect.job_name, data_list)
        #     data_list.append(new_prepare_data(os.path.join('csv_files', file), InputConnect.job_name))
        #
        # for data in data_list:
        #     year = data[0]
        #     salary_by_years[year] = data[1]
        #     vacs_by_years[year] = data[2]
        #     job_salary_by_years[year] = data[3]
        #     job_count_by_years[year] = data[4]

        finish_time = time.time()

        df['salary_from'] = df['salary_currency'].map(currency_to_rub) * df['salary_from']
        df['salary_to'] = df['salary_currency'].map(currency_to_rub) * df['salary_to']
        df['salary'] = df[['salary_from', 'salary_to']].mean(axis=1)

        area = df['area_name'].value_counts().to_dict()
        area = dict(sorted(area.items(), key=lambda x: x[1], reverse=True))
        vacs_sum = len(df)
        result_city = [city for city in area.keys() if area[city] / vacs_sum > 0.01]
        salary_by_cities = {}
        vacs_by_cities = {}

        i = 0
        while i < 10:
            city = result_city[i]
            salary_by_cities[city] = mean_to_number(df[df['area_name'] == city]['salary'].mean())
            vacs_by_cities[city] = round((len(df[df['area_name'] == city]) / vacs_sum), 4)
            i += 1

        # for p in process:
        #     p.join()

        # for data in data_list:
        #     year = data[0]
        #     salary_by_years[year] = data[1]
        #     vacs_by_years[year] = data[2]
        #     job_salary_by_years[year] = data[3]
        #     job_count_by_years[year] = data[4]

        print('Динамика уровня зарплат по годам:', salary_by_years)
        print('Динамика количества вакансий по годам:', vacs_by_years)
        print('Динамика уровня зарплат по годам для выбранной профессии:', job_salary_by_years)
        print('Динамика количества вакансий по годам для выбранной профессии:', job_count_by_years)
        print('Уровень зарплат по городам (в порядке убывания):', salary_by_cities)
        print('Доля вакансий по городам (в порядке убывания):', vacs_by_cities)

        print('Суммарное время равно: ' + str((finish_time - startime)) + ' секунд')


if __name__ == '__main__':
    # cProfile.run('InputConnect()', 'restats')
    # p = Stats('restats')
    # p.sort_stats(SortKey.TIME).print_stats(1)
    InputConnect()
