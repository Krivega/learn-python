from __future__ import annotations


def validate(value):
    try:
        isValidByType = isinstance(int(value), int)
        return isValidByType
    except Exception:
        return False


def task(value):
    result = value % 5 if value > 5 else 0

    return result
