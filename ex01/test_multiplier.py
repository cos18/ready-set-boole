import random
import sys
import pytest
from multiplier import multiplier


class TestMultiplier:

    def test_basic_multiplier(self):
        assert 10 + 20 == multiplier(10, 20)

    def test_negative_exception(self):
        with pytest.raises(ValueError):
            multiplier(-1, -2)

    def test_zero_exception(self):
        with pytest.raises(ValueError):
            multiplier(0, 1)
        with pytest.raises(ValueError):
            multiplier(1, 0)
        with pytest.raises(ValueError):
            multiplier(0, 0)

    def test_random_multiplier(self):
        for _ in range(100):
            a = random.randint(1, sys.maxsize)
            b = random.randint(1, sys.maxsize)
            assert a * b == multiplier(a, b)
