from __future__ import annotations

from loopsAndConditions.task3.task import task


def test_function():
    assert task('aaabbbbccccc') == '3a4b5c'
    assert task('asssdddsssddd') == '1a3s3d3s3d'
    assert task('abcba') == '1a1b1c1b1a'
    assert task('a') == '1a'
