from __future__ import annotations

import string


def task(value: str, shift: int):
    result = ''

    for char in value:
        if not char.isalpha():
            result += char
            continue
        position = string.ascii_lowercase.index(char.lower())
        nextPosition = (position + shift) % len(string.ascii_lowercase)
        result += (
            string.ascii_lowercase[nextPosition] if char.islower() else string.ascii_uppercase[nextPosition]
        )

    return result
