from __future__ import annotations

from function1.task1.task import task


def test_function():
    assert task('') == ''
    assert task(' ') == ' '
    assert task('otus_course') == 'OtusCourse'
    assert task('PythonIsTheBest') == 'python_is_the_best'
    assert task('otus_course', direction='auto') == 'OtusCourse'
    assert task('PythonIsTheBest', direction='auto') == 'python_is_the_best'
    assert task('PythonIsTheBest', direction='snake') == 'python_is_the_best'
    assert task('python_is_the_best', direction='snake') == 'python_is_the_best'
    assert task('python_is_the_best', direction='camel') == 'PythonIsTheBest'
    assert task('PythonIsTheBest', direction='camel') == 'PythonIsTheBest'
