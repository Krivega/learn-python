from __future__ import annotations


def task(value: str):
    size = len(value)
    result = ''
    count = 1
    prevChar = value[0]

    for index in range(size):
        char = value[index + 1] if index < size - 1 else ''

        if char == prevChar:
            count += 1
        else:
            result += str(count) + prevChar
            count = 1
            prevChar = char

    return result
