from __future__ import annotations

from loopsAndConditions.task1.task import task


def test_function():
    assert task('1') == 1
    assert task('10') == 1
    assert task('11') == 2
    assert task('545') == 5
    assert task('12345') == 6
    assert task('30789') == 9
