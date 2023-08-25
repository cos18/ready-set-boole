import random
import sys
import pytest
from adder import adder


class TestAdder:

    def test_basic_addition(self):
        assert 10 + 20 == adder(10, 20)

    def test_negative_exception(self):
        with pytest.raises(ValueError):
            adder(-1, -2)

    def test_zero_exception(self):
        with pytest.raises(ValueError):
            adder(0, 1)
        with pytest.raises(ValueError):
            adder(1, 0)
        with pytest.raises(ValueError):
            adder(0, 0)

    def test_random_addition(self):
        for _ in range(100):
            a = random.randint(1, sys.maxsize)
            b = random.randint(1, sys.maxsize)
            assert a + b == adder(a, b)
