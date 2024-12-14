from __future__ import annotations

from immutableTypes.task1.task import task


def test_function():
    assert task('123456') == '154326'
    assert task('23456') == '25436'
    assert task('30789') == '38709'
