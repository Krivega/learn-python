from __future__ import annotations


def camelToSnakeCase(inputValue: str) -> str:
    result = ''

    for i in range(len(inputValue)):
        letter = inputValue[i]
        if letter.isupper() and i > 0:
            result += '_'
        result += letter.lower()

    return result


def snakeToCamelCase(inputValue: str) -> str:
    words = inputValue.split('_')
    result = ''.join(word.title() for word in words)

    return result


def task(inputValue: str) -> bool:
    if len(inputValue) < 5:
        return False

    day, month, year = inputValue.split('.')

    if not day.isdigit() or not month.isdigit() or not year.isdigit():
        return False

    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        return False

    if int(day) > 31 or int(month) > 12:
        return False

    if (int(month) == 2 and int(day) > 29) or (
        int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11 and int(day) > 30
    ):
        return False

    if (not int(year) % 4 == 0 and int(year) % 100 != 0) and not (int(year) % 400 == 0):
        if int(month) == 2 and int(day) > 28:
            return False

    return True
