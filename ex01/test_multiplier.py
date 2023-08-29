import random
import pytest
from multiplier import multiplier


class TestMultiplier:
    u32_max = 4294967295

    def test_basic_multiplier(self):
        assert multiplier(10, 20) == 10 * 20

    def test_negative_exception(self):
        with pytest.raises(ValueError):
            multiplier(-1, -2)

    def test_over_range_exception(self):
        with pytest.raises(ValueError):
            multiplier(0, self.u32_max + 1)
        with pytest.raises(ValueError):
            multiplier(self.u32_max + 1, 0)
        with pytest.raises(ValueError):
            multiplier(self.u32_max + 1, self.u32_max + 1)

    def test_random_multiplier(self):
        for _ in range(100):
            a = random.randint(1, self.u32_max)
            b = random.randint(1, self.u32_max)
            assert multiplier(a, b) == a * b
