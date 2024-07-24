from exceptions import division
import pytest

def test_valid():
    assert division(10,2)==5
    assert division(5,2) == 2.5

def test_invalid():
    with pytest.raises(ValueError):
        division(4,0)
    with pytest.raises(TypeError):
        division(4,'a')
    with pytest.raises(TypeError):
        division('a',4)
    with pytest.raises(TypeError):
        division('b',0)

#If there are two types of errors, the first one stated in the code is the error. Here, in exceptions.py, the TypeError was coded first thus it is a TypeError.