import random
import pytest
from adder import adder


class TestAdder:
    u32_max = 4294967295

    def test_basic_addition(self):
        assert adder(10, 20) == 10 + 20

    def test_zero_addition(self):
        for _ in range(100):
            a = random.randint(0, self.u32_max)
            assert adder(a, 0) == a

    def test_negative_exception(self):
        with pytest.raises(ValueError):
            adder(-1, -2)

    def test_over_range_exception(self):
        with pytest.raises(ValueError):
            adder(0, self.u32_max + 1)
        with pytest.raises(ValueError):
            adder(self.u32_max + 1, 0)
        with pytest.raises(ValueError):
            adder(self.u32_max + 1, self.u32_max + 1)

    def test_random_addition(self):
        for _ in range(100):
            a = random.randint(0, self.u32_max)
            b = random.randint(0, self.u32_max)
            assert adder(a, b) == a + b
