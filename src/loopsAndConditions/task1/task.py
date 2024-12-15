from __future__ import annotations


def validate(value: str):
    try:
        isValidByType = isinstance(int(value), int)
        return isValidByType
    except Exception:
        return False


def task(value: str):
    result = value

    while len(result) > 1:
        result = f'{int(result[0]) + int(result[1])}{result[2:]}'
    return int(result)
