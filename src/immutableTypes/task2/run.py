from __future__ import annotations

from immutableTypes.task2.task import task, validate

inputValue = input('Введите число:')

if not validate(inputValue):
    print('Вы ввели не число')
    exit()

result = task(int(inputValue))

print(result)
