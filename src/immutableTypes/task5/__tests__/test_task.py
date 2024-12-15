from __future__ import annotations

from immutableTypes.task5.task import task


def test_function():
    assert task('5.6') is True
    assert task('.78') is True
    assert task('.67.') is False
    assert task('5') is True
