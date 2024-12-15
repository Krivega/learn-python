from __future__ import annotations

from immutableTypes.task5.task import task, validate

inputValue = input('Введите строку:')


if not validate(inputValue):
    print('Вы ввели не верный формат')
    exit()


result = task(inputValue)

print(result)
