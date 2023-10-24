from nnf import negation_normal_form


class TestNNF:

    def test_basic_nnf(self):
        assert negation_normal_form('AB&!') == 'A!B!|'
        assert negation_normal_form('AB|!') == 'A!B!&'
        assert negation_normal_form('AB>') == 'A!B|'
        assert negation_normal_form('AB=') == 'AB&A!B!&|'
        assert negation_normal_form('AB|C&!') == 'A!B!&C!|'
