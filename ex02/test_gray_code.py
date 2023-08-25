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
