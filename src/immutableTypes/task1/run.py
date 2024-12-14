from __future__ import annotations

from immutableTypes.task1.task import task, validate

inputValue = input('Введите пятизначное число:')

if not validate(inputValue):
    print('Вы ввели не пятизначное число')
    exit()


result = task(inputValue)

print(result)
