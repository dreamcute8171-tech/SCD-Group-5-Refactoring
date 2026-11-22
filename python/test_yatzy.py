from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual        

def test_score_pair():
    expected = 10
    actual = Yatzy.score_pair(2, 3, 5, 5, 1)
    assert expected == actual

def test_number_categories():
    assert Yatzy.ones(1, 2, 1, 4, 5) == 2
    assert Yatzy.twos(2, 2, 1, 4, 5) == 4
    assert Yatzy.threes(3, 3, 3, 4, 5) == 9

    game = Yatzy(4, 4, 5, 6, 1)
    assert game.fours() == 8
    assert game.fives() == 5
    assert game.sixes() == 6