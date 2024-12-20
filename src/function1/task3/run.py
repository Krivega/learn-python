from __future__ import annotations

from function1.task3.task import task, validate

inputValue = input('Введите число:')

if not validate(inputValue):
    print('Вы ввели не число')
    exit()


result = task(int(inputValue))

if result is True:
    print('Число является простым')
else:
    print('Число не является простым')
