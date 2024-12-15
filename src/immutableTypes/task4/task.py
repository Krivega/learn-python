from __future__ import annotations


def validate(value):
    try:
        isValidByType = isinstance(int(value), int)
        return isValidByType
    except Exception:
        return False


ROME_DIC = (('I', 'V', 'X'), ('X', 'L', 'C'), ('C', 'D', 'M'), ('M', '', ''))


def task(value):
    result = ''
    size = len(value)

    for i in range(size):
        discharge = size - 1 - i
        romeDicByDischarge = ROME_DIC[i]
        item = int(value[discharge])

        if item == 0:
            continue
        elif item < 4:
            result = romeDicByDischarge[0] * item + result
        elif item == 4:
            result = romeDicByDischarge[0] + romeDicByDischarge[1] + result
        elif item == 5:
            result = romeDicByDischarge[1] + result
        elif item < 9:
            result = romeDicByDischarge[1] + romeDicByDischarge[0] * (item - 5) + result
        elif item == 9:
            result = romeDicByDischarge[0] + romeDicByDischarge[2] + result
    return result
