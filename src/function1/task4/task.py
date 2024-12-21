from __future__ import annotations

from enum import Enum, unique

SIZE_ID = 8
EXPECTED_INPUT_SIZE = 4


def validateFormatInputValue(inputValue: str) -> bool:
    try:
        if len(inputValue.strip()) == 0:
            return True

        values = inputValue.split(' ')
        isValidBySize = len(values) == EXPECTED_INPUT_SIZE
        firstName, lastName, age, id = values
        isValidFirstNameBySize = len(firstName) > 0
        isValidLastNameBySize = len(lastName) > 0
        isValidAgeByType = isinstance(int(age), int)
        isValidIDByType = isinstance(int(id), int)
        isValidIDBySize = len(id) == SIZE_ID

        return (
            isValidBySize
            and isValidFirstNameBySize
            and isValidFirstNameBySize
            and isValidLastNameBySize
            and isValidAgeByType
            and isValidIDBySize
            and isValidIDByType
        )
    except Exception:
        return False


@unique
class Errors(Enum):
    WRONG_AGE_RANGE = 'WRONG_AGE_RANGE'
    DUPLICATE_ID = 'DUPLICATE_ID'


db = {}


def validateDataValues(age: int, id: str) -> Errors | None:
    if age < 18 or age > 60:
        return Errors.WRONG_AGE_RANGE
    if id in db:
        return Errors.DUPLICATE_ID

    return None


def formatError(error: Errors) -> str:
    if error == Errors.WRONG_AGE_RANGE:
        return 'Возраст должен быть числом от 18 до 60'
    if error == Errors.DUPLICATE_ID:
        return 'Такой ID уже существует'

    return 'Неизвестная ошибка'


def write(firstName: str, lastName: str, age: int, id: str):
    db[id] = (firstName.capitalize(), lastName.capitalize(), age)


def getTableFromDB():
    table = []
    for id, value in db.items():
        firstName, lastName, age = value
        table.append([id, firstName, lastName, age])
    return table
