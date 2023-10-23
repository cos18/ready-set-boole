import pytest
from eval_formula import eval_formula


class TestGrayCode:

    def test_simple_value(self):
        assert eval_formula('1') == True
        assert eval_formula('0') == False

    def test_examples(self):
        assert eval_formula('10&') == False
        assert eval_formula('10|') == True
        assert eval_formula('11>') == True
        assert eval_formula('10=') == False
        assert eval_formula('1011||=') == True

    def test_wrong_formular(self):
        with pytest.raises(ValueError):
            eval_formula('test')
        with pytest.raises(ValueError):
            eval_formula('101|')
        with pytest.raises(ValueError):
            eval_formula('23=')
        with pytest.raises(ValueError):
            eval_formula('^10')
        with pytest.raises(ValueError):
            eval_formula('!!!!!01')