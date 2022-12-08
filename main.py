"""
Этот модуль нужен для объединения работы модуля по формированию отчетов
и модуль по табличной печати вакансий
"""

import report_out_old
import table_out


type_out = input('Введите данные для печати: ')
if type_out == 'Вакансии':
    table_out.InputConnect()
elif type_out == 'Статистика':
    report_out_old.InputConnect()
else:
    print('Некорректный ввод!')