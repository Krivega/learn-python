from __future__ import annotations

from loopsAndConditions.task2.task import task


def test_function():
    assert task([[0, 1, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]], 2) == 1
    assert task([[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1]], 2) is False
