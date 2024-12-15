from __future__ import annotations

from loopsAndConditions.task1.task import task, validate

inputValue = input('Введите число:')

if not validate(inputValue):
    print('Вы ввели не число')
    exit()


result = task(inputValue)

print(result)
