from __future__ import annotations


def validate(value: str):
    try:
        isValidByType = isinstance(int(value), int)
        return isValidByType
    except Exception:
        return False


def task(number: int) -> bool:
    if number < 2:
        return False

    i = 2

    while i * i <= number:
        if number % i == 0:
            return False
        i = i + 1

    return True
