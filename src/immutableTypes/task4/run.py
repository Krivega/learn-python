from __future__ import annotations

from immutableTypes.task4.task import task, validate

inputValue = input('Введите число:')


if not validate(inputValue):
    print('Вы ввели не верный формат')
    exit()


result = task(inputValue)

print(result)
