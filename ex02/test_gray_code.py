import random
import sys
import pytest
from gray_code import gray_code


class TestGrayCode:

    def test_examples(self):
        assert gray_code(0) == 0
        assert gray_code(1) == 1
        assert gray_code(2) == 3
        assert gray_code(3) == 2
        assert gray_code(4) == 6
        assert gray_code(5) == 7
        assert gray_code(6) == 5
        assert gray_code(7) == 4
        assert gray_code(8) == 12

    def test_negative_exception(self):
        with pytest.raises(ValueError):
            gray_code(-1)

    def test_return_value_satisfy_rule(self):
        for _ in range(10000):
            tmp = random.randint(0, sys.maxsize)
            tmp_result = gray_code(tmp)
            next_result = gray_code(tmp + 1)
            check = 0
            while tmp_result or next_result:
                if (tmp_result & 1) ^ (next_result & 1):
                    check += 1
                tmp_result >>= 1
                next_result >>= 1
            if check != 1:
                assert False  # disjoint two numbers aren't different with 1 bit only
