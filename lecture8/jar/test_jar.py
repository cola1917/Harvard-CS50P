from jar import Jar
import pytest


def test_init():
    jar = Jar(1)
    jar = Jar(0)
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(0)
    assert jar.size == 1
    jar.deposit(9)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.withdraw(1)
    jar.deposit(10)
    assert jar.size == 10
    jar.withdraw(1)
    assert jar.size == 9
    jar.withdraw(2)
    assert jar.size == 7
