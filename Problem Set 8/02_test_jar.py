from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(20)

def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.withdraw(20)
