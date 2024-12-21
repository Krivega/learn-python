from __future__ import annotations

from enum import Enum


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


class Direction(Enum):
    auto = 'auto'
    snake = 'snake'
    camel = 'camel'


def task(inputValue: str, direction: Direction = 'auto') -> str:
    if len(inputValue) == 0:
        return inputValue

    isCamelInputValue = inputValue[0].isupper()
    isSnakedInputValue = '_' in inputValue

    if (direction == 'auto' and isCamelInputValue) or (direction == 'snake' and isCamelInputValue):
        return camelToSnakeCase(inputValue)
    elif (direction == 'auto' and isSnakedInputValue) or (direction == 'camel' and isSnakedInputValue):
        return snakeToCamelCase(inputValue)

    return inputValue
