import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    # Intentionally wrong assertion to fail the build (2 + 3 != 99)
    assert add(2, 3) == 99
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 4) == -4

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(5, 0)