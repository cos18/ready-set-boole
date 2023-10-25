import pytest
from truth_table import print_truth_table


class TestTruthTable:

    def test_simple_table(self, capsys):
        print_truth_table('O!!')
        captured = capsys.readouterr()
        assert captured.out == \
'''| O | = |
|---|---|
| 0 | 0 |
| 1 | 1 |
'''

    def test_various_variables_table(self, capsys):
        print_truth_table('AB&C|')
        captured = capsys.readouterr()
        assert captured.out == \
'''| A | B | C | = |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |
'''

        print_truth_table('XA&Z|')
        captured = capsys.readouterr()
        assert captured.out == \
'''| A | X | Z | = |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |
'''

    def test_wrong_formular(self):
        with pytest.raises(ValueError):
            print_truth_table('test')
        with pytest.raises(ValueError):
            print_truth_table('ABC|')
        with pytest.raises(ValueError):
            print_truth_table('Bc=')
        with pytest.raises(ValueError):
            print_truth_table('^AB')
        with pytest.raises(ValueError):
            print_truth_table('!!!!!AB')
