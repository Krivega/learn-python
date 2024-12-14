from __future__ import annotations

from immutableTypes.task3.task import task


def test_function():
    assert task(3, 4, 6) is True
    assert task(3, 1, 6) is False
    assert task(5, 7, 8) is False
    assert task(4, 5, 12) is True
