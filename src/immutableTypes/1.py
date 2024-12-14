from __future__ import annotations


def validate(value):
    try:
        isValidByLen = len(value) == 5
        isValidByType = isinstance(int(value), int)
        return isValidByLen and isValidByType
    except Exception:
        return False


inputValue = input('Введите пятизначное число:')

if not validate(inputValue):
    print('Вы ввели не пятизначное число')
    exit()

firstPart = inputValue[0]
middlePart = inputValue[1:-1]
lastPart = inputValue[-1]
middlePartReversed = middlePart[::-1]

result = f'{firstPart}{middlePartReversed}{lastPart}'
print(result)
