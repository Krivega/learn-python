from __future__ import annotations

from immutableTypes.task2.task import task


def test_function():
    assert task(4) == 0
    assert task(6) == 1
    assert task(14) == 4
