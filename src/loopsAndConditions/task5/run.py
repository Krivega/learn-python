from __future__ import annotations

from loopsAndConditions.task5.task import task, validate

values = []

while True:
    inputValue = input(
        'Введите через пробел название предмета, фамилию ученика и оценку, для завершения введите пустую строку:'
    )

    if not validate(inputValue):
        print('Вы ввели не верный формат')
        exit()

    if inputValue == '':
        break

    values.append(inputValue)


result = task(values)


for item in result:
    print(item)
