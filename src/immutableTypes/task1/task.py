from __future__ import annotations


def validate(value):
    try:
        isValidByLen = len(value) == 5
        isValidByType = isinstance(int(value), int)
        return isValidByLen and isValidByType
    except Exception:
        return False


def task(value):
    firstPart = value[0]
    middlePart = value[1:-1]
    lastPart = value[-1]
    middlePartReversed = middlePart[::-1]

    result = f'{firstPart}{middlePartReversed}{lastPart}'

    return result
