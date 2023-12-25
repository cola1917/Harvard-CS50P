import pytest
from numb3rs import validate

def test_validate():
    assert validate('255.255.255.255') == True
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate('cat') == False

def test_range():
    assert validate(r"255.255.255.255")==True
    assert validate(r"512.1.1.1")==False
    assert validate(r"1.512.1.1")==False
    assert validate(r"1.1.512.1")==False
    assert validate(r"1.1.1.512")==False
