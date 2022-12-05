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
