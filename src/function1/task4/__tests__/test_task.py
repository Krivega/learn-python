from __future__ import annotations

from function1.task4.task import (
    Errors,
    formatError,
    getTableFromDB,
    validateDataValues,
    validateFormatInputValue,
    write,
)


def test_validateFormatInputValue():
    assert validateFormatInputValue('name sec 20 12345673') is True
    assert validateFormatInputValue('name sec 20 1234567') is False
    assert validateFormatInputValue('name sec 20 1234567 ') is False
    assert validateFormatInputValue('name sec 20') is False
    assert validateFormatInputValue('name sec 20 1') is False
    assert validateFormatInputValue('name sec 20 1234567 1234567') is False
    assert validateFormatInputValue('') is True
    assert validateFormatInputValue(' ') is True


def test_Write():
    write(firstName='name', lastName='sec', age=18, id='12345678')
    write(firstName='name2', lastName='sec2', age=18, id='12345671')

    assert getTableFromDB() == [['12345678', 'Name', 'Sec', 18], ['12345671', 'Name2', 'Sec2', 18]]


def test_validateDataValues():
    assert validateDataValues(age=18, id='02345678') is None
    assert validateDataValues(age=17, id='02345678') == Errors.WRONG_AGE_RANGE
    assert validateDataValues(age=61, id='02345678') == Errors.WRONG_AGE_RANGE

    write(firstName='name', lastName='sec', age=18, id='02345678')

    assert validateDataValues(age=18, id='02345678') is Errors.DUPLICATE_ID


def test_formatError():
    assert formatError('asd') == 'Неизвестная ошибка'
    assert formatError(Errors.WRONG_AGE_RANGE) == 'Возраст должен быть числом от 18 до 60'
    assert formatError(Errors.DUPLICATE_ID) == 'Такой ID уже существует'
