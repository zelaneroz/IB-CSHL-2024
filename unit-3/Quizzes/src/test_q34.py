from q34 import to_roman
import pytest

def test_to_roman():
    assert to_roman(1) == 'I'
    assert to_roman(4) == 'IV'
    assert to_roman(9) == 'IX'
    assert to_roman(37) == 'XXXVII'
    assert to_roman(44) == 'XLIV'
    assert to_roman(50) == 'L'
    assert to_roman(99) == 'XCIX'
    assert to_roman(100) == 'C'
    assert to_roman(77) == 'LXXVII'
    assert to_roman(93) == 'XCIII'


def test_to_roman_exceptions():
    # check that the program raises a ValueError
    with pytest.raises(ValueError):
        to_roman(101)