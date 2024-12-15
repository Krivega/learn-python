from __future__ import annotations


def validate(value):
    try:
        isValidBySize = len(value) > 0
        return isValidBySize
    except Exception:
        return False


NUMBERS = frozenset('0123456789')


def task(value):
    isValid = True
    countDots = 0

    for char in value:
        isDot = char == '.'
        if not isDot and char not in NUMBERS:
            isValid = False
            break
        elif isDot and (countDots > 0):
            isValid = False
            break
        elif isDot:
            countDots += 1

    return isValid
