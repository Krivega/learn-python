from __future__ import annotations

from immutableTypes.task4.task import task


def test_function():
    assert task('1') == 'I'
    assert task('4') == 'IV'
    assert task('5') == 'V'
    assert task('6') == 'VI'
    assert task('8') == 'VIII'
    assert task('9') == 'IX'
    assert task('10') == 'X'
    assert task('11') == 'XI'
    assert task('15') == 'XV'
    assert task('16') == 'XVI'
    assert task('18') == 'XVIII'
    assert task('19') == 'XIX'
    assert task('20') == 'XX'
    assert task('50') == 'L'
    assert task('100') == 'C'
    assert task('234') == 'CCXXXIV'
    assert task('500') == 'D'
    assert task('559') == 'DLIX'
    assert task('1000') == 'M'
    assert task('2345') == 'MMCCCXLV'
    assert task('2000') == 'MM'
    assert task('3000') == 'MMM'
