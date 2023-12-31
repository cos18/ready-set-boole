from cnf import conjunctive_normal_form


class TestCNF:

    def test_basic_cnf(self):
        assert conjunctive_normal_form('AB&!') == 'A!B!|'
        assert conjunctive_normal_form('AB|!') == 'A!B!&'
        assert conjunctive_normal_form('AB|C&') == 'AB|C&'
        assert conjunctive_normal_form('AB|C|D|') == 'ABCD|||'
        assert conjunctive_normal_form('AB&C&D&') == 'ABCD&&&'
        assert conjunctive_normal_form('AB&!C!|') == 'A!B!C!||'
        assert conjunctive_normal_form('AB|!C!&') == 'A!B!C!&&'

    def test_tough_cnf(self):
        assert conjunctive_normal_form('AB&CD&|') == 'AC|BC|AD|BD|&&&'
        assert conjunctive_normal_form('AB&C|D|E|') == 'ACDE|||BCDE|||&'
