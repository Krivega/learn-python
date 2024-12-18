from __future__ import annotations


def validate(value: str):
    try:
        isValidByLen = len(value) == 3
        isValidByType = all(isinstance(int(item), int) for item in value)
        return isValidByLen and isValidByType
    except Exception:
        return False


def task(width: int, height: int, targetSize: int):
    square = width * height
    isAvailableBySquare = targetSize <= square
    if not isAvailableBySquare:
        return False

    isValidByWidth = targetSize % width == 0
    isValidByHeight = targetSize % height == 0

    return isValidByWidth or isValidByHeight
