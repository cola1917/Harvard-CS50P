from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("3/4") == 75
    assert convert("0/100") == 0
    assert convert("100/100") == 100
    assert convert("99/100") == 99

    with pytest.raises(ValueError):
        convert("x/y")
    # with pytest.raises(ValueError):
    #     convert("10/1")
    # with pytest.raises(ValueError):
    #     convert("x")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(2) == "2%"
    # with pytest.raises(ValueError):
    #     gauge(101)
    # with pytest.raises(TypeError):
    #     gauge('x')

