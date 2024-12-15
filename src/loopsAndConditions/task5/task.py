from __future__ import annotations


def validate(value: str):
    try:
        if value == '':
            return True
        isValidBySize = len(value.split(' ')) == 3
        isValidByType = isinstance(int(value[-1]), int)
        return isValidBySize and isValidByType
    except Exception:
        return False


def task(value: list[str]):
    dictatory = {}

    for line in value:
        subject, student, grade = line.split(' ')

        if subject not in dictatory:
            dictatory[subject] = {}

        if student not in dictatory[subject]:
            dictatory[subject][student] = []

        dictatory[subject][student].append(grade)

    result = []
    subjects = list(dictatory.keys())

    for subject in subjects:
        result.append(subject)

        for student in dictatory[subject]:
            grades = ' '.join(dictatory[subject][student])
            result.append(f'{student} {grades}')

        isLastSubject = subjects[-1] == subject
        if not isLastSubject:
            result.append('')

    return result
