from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual        

def test_chance():
    expected = 15
    actual = Yatzy.chance(1, 2, 3, 4, 5)
    assert expected == actual
