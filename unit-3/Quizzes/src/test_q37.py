import pytest
from q37 import AccountingProgram

def test_calculate_interest():
    program = AccountingProgram()
    program.set_principal(1000)
    program.set_rate(0.05)
    program.set_years(10)
    interest = program.calculate_interest()
    assert interest == 1628.89

def test_principal_validation():
    program = AccountingProgram()
    with pytest.raises(ValueError) as err:
        program.set_principal(-1000)
    assert "Principal should be greater than zero" in str(err.value)

def test_rate_validation():
    program = AccountingProgram()
    with pytest.raises(ValueError) as err:
        program.set_rate(-0.05)
    assert "Interest rate should be greater than zero" in str(err.value)

def test_years_validation():
    program = AccountingProgram()
    with pytest.raises(ValueError) as err:
        program.set_years(-10)
    assert "Years should be greater than zero" in str(err.value)