from __future__ import annotations

from function1.task3.task import task


def test_function():
    assert task(1) is False
    assert task(2) is True
    assert task(3) is True
    assert task(4) is False
    assert task(5) is True
    assert task(6) is False
    assert task(7) is True
    assert task(8) is False
