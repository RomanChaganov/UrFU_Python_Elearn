"""
Этот модуль нужен для объединения работы модуля по формированию отчетов
и модуль по табличной печати вакансий
"""

import report_out
import table_out

type_out = input('Введите данные для печати: ')
if type_out == 'Вакансии':
    table_out.InputConnect()
elif type_out == 'Статистика':
    report_out.InputConnect()
else:
    print('Некорректный ввод!')