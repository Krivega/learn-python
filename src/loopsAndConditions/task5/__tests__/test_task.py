from __future__ import annotations

from loopsAndConditions.task5.task import task


def test_function():
    actual = task(
        [
            'Математика Иванов 5',
            'Математика Иванов 4',
            'Литература Иванов 3',
            'Математика Петров 5',
            'Литература Сидоров 3',
            'Литература Петров 5',
            'Литература Иванов 4',
            'Математика Сидоров 3',
            'Математика Петров 5',
        ]
    )
    expected = [
        'Математика',
        'Иванов 5 4',
        'Петров 5 5',
        'Сидоров 3',
        '',
        'Литература',
        'Иванов 3 4',
        'Сидоров 3',
        'Петров 5',
    ]

    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])
