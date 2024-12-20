from __future__ import annotations

from function1.task2.task import task


def test_function():
    # assert task('') is False
    # assert task(' ') is False
    assert task('29.02.2000') is True
    # assert task('29.0220.00') is False
    # assert task('29.02.2001') is False
    # assert task('31.04.1962') is False
