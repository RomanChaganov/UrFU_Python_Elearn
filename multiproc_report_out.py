import multiprocessing
from report_out_old import formatter_date
import pandas as pd


class MultiInputConnect:
    def __init__(self, file_name):
        pd.set_option('expand_frame_repr', False)

    @staticmethod
    def data_preparation(file_name):
        df = pd.read_csv(file_name)
        df['published_at'] = df['published_at'].apply(formatter_date)
        df['salary'] = df[['salary_from', 'salary_to']].mean(axis=1)
        year = df['published_at'].values(0)


