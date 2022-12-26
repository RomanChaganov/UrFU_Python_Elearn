import pandas as pd
import numpy as np

pd.set_option('expand_frame_repr', False)

currency_data = pd.read_csv('Currency_data.csv')
currency_data = currency_data.set_index('date')
print('Подгрузка файла по валютам\n')
print(currency_data.head())
currency = list(currency_data.columns)

df = pd.read_csv('vacancies_dif_currencies.csv')
print('Открытие файла по вакансиям')
df.salary_from = df[['salary_from', 'salary_to']].mean(axis=1)
df['date'] = df.published_at.apply(lambda z: z[:7])
df['salary_from'] = df.apply(
    lambda x: float(round(x['salary_from'] * currency_data.at[x['date'], x['salary_currency']]))
    if (x['salary_currency'] != 'RUR' and not np.isnan(x['salary_from']) and x['salary_currency'] in currency)
    else x['salary_from'], axis=1)


df = df.drop(['salary_to', 'date', 'salary_currency'], axis=1).rename(columns={'salary_from':'salary'})
df.head(100).to_csv('first100vacancies.csv', index=False)
