# Тесты и замеры времени работы программы
## Тесты doctest и unittest
Я написал doctest в файле report_out к методам, к которым это было возможно.
А юнит тесты к файлу table_out к методам по фильтрации и сортировки

![Doctests](https://github.com/RomanChaganov/UrFU_Python_Elearn/blob/main/image/doctests.png)
![Unittests](https://github.com/RomanChaganov/UrFU_Python_Elearn/blob/main/image/unittests.png)

## Замер времени исполнения программы и выявление самых продолжительно-работающих функций
Замерил время работы модуля report_out. Суммарное время составило около 138 секунд. Самая долгая функция - это функция преобразования времени из модуля datetime.

![First_measurement](https://github.com/RomanChaganov/UrFU_Python_Elearn/blob/main/image/datetime_one.png)

Измерил функцию преобразования времени отдельно и получил значение 0.007 секунд.

![Func_measurement](https://github.com/RomanChaganov/UrFU_Python_Elearn/blob/main/image/func_date.png)

Измерил второй вариант функции и получил 0 секунд.

![Firts_analog](https://github.com/RomanChaganov/UrFU_Python_Elearn/blob/main/image/one_analog.png)

Третий вариант показал такие же результаты.

![Second_analog](https://github.com/RomanChaganov/UrFU_Python_Elearn/blob/main/image/second_analog.png)

Оставив в результате самую быструю функцию, получилось сократить время работы программы до 38 секунд.

![Finish_measurement](https://github.com/RomanChaganov/UrFU_Python_Elearn/blob/main/image/finish_test.png)

# Разделение данных и паралелльные вычисления

## Разделение данных
С помощью скрипта разделил исходный файл на файлы

![Data_split](https://github.com/RomanChaganov/UrFU_Python_Elearn/blob/main/image/data_from_years.png)

## Многопроцессорность
Замер времени работы программы проводился с помощью функции time().
Для однопроцессорного режима время работы составила 14.27 секунд

![Without_multiproc](https://github.com/RomanChaganov/UrFU_Python_Elearn/blob/main/image/without_multiproc.png)

Многопроцессорность достигалась благодаря функции Pool().
Время работы составила 13.57 секунд. Виден небольшой прирост.

![Multiprocc](https://github.com/RomanChaganov/UrFU_Python_Elearn/blob/main/image/multiproc.png)

С помощью асинхронности удалось сбить 11 миллисекунд.
Время работы составила 13.46 секунды.

![Concurrent](https://github.com/RomanChaganov/UrFU_Python_Elearn/blob/main/image/concurrent.png)

# Получение валют 
## Получение данных о валютах с сайта ЦБ РФ
Получил данные о частотности валют

![Frequency](https://github.com/RomanChaganov/UrFU_Python_Elearn/blob/main/image/frequency.png)

Разделил полученные котировки по годам

![Currency_data](https://github.com/RomanChaganov/UrFU_Python_Elearn/blob/main/image/split_currency_data.png)

# База данных
## К заданию 3.5.2

![DataBase](https://github.com/RomanChaganov/UrFU_Python_Elearn/blob/main/image/sqlite.png)

## К заданию 3.5.3
Скрин БД. Пришлось изменить прошлый скрипт, чтобы он сохранял дату, в формате нужном для strftime.

![DB](https://github.com/RomanChaganov/UrFU_Python_Elearn/blob/main/image/db.png)

Скрин кода и результата работы.

![Code](https://github.com/RomanChaganov/UrFU_Python_Elearn/blob/main/image/code.png)