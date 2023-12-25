from plates import is_valid
# is_valid("CS50")

def test_plates():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("123456") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("OUTAT") == True
    assert is_valid("OUTATI") == True
