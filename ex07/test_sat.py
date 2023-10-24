from sat import sat


class TestSAT:

    def test_basic_sat(self):
        assert sat('AB|') == True
        assert sat('AB&') == True
        assert sat('AA!&') == False
        assert sat('AA^') == True
