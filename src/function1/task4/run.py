from __future__ import annotations

from function1.task4.task import (
    formatError,
    getTableFromDB,
    validateDataValues,
    validateFormatInputValue,
    write,
)

while True:
    inputValue = input(
        'Введите через пробел название имя, фамилию, возраст и ID, для завершения введите пустую строку:\n'
    )

    if not validateFormatInputValue(inputValue):
        print('Вы ввели не верный формат')
        continue

    if len(inputValue.strip()) == 0:
        break

    firstName, lastName, age, id = inputValue.strip().split(' ')

    error = validateDataValues(age=int(age), id=id)

    if error is not None:
        print(formatError(error))
        continue

    write(firstName=firstName, lastName=lastName, age=int(age), id=id)


table = getTableFromDB()

print(table)


def printRow(row: list[str | int]):
    print('| {:1} | {:^4} | {:>4} | {:<3} |'.format(*row))


printRow(['ID', 'Имя', 'Фамилия', 'Возраст'])

for row in table:
    printRow(row)
