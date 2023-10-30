from nnf import negation_normal_form
from NNFBoolAST import BoolAST


class TestBoolAST:

    def test_str(self):
        assert str(BoolAST('AB&!')) == 'AB&!'
        assert str(BoolAST('AB|C&!')) == 'AB|C&!'


class TestNNF:

    def test_basic_nnf(self):
        assert negation_normal_form('AB&!') == 'A!B!|'
        assert negation_normal_form('AB|!') == 'A!B!&'
        assert negation_normal_form('AB>') == 'A!B|'
        assert negation_normal_form('AB=') == 'AB&A!B!&|'
        assert negation_normal_form('AB|C&!') == 'A!B!&C!|'

    def test_tough_nnf(self):
        assert negation_normal_form('A!!!!') == 'A'
        assert negation_normal_form('A!!!B!!!!!&') == 'A!B!&'
