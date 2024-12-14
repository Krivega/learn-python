from __future__ import annotations

from immutableTypes.task3.task import task, validate

inputValue = input('Введите через запятую длину, ширину размер куска:')

values = inputValue.split(',')
valuesStripped = list(map(str.strip, values))

if not validate(valuesStripped):
    print('Вы ввели не верный формат')
    exit()


[width, height, targetSize] = list(map(int, valuesStripped))

result = task(width, height, targetSize)

print(result)
