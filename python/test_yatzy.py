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

def test_two_pair():
    assert Yatzy.two_pair(2, 2, 3, 3, 5) == 10
    assert Yatzy.two_pair(1, 1, 4, 4, 6) == 10
    assert Yatzy.two_pair(2, 2, 2, 3, 4) == 0

def test_three_and_four_of_a_kind():
    assert Yatzy.three_of_a_kind(3, 3, 3, 4, 5) == 9
    assert Yatzy.three_of_a_kind(5, 5, 5, 5, 2) == 15

    assert Yatzy.four_of_a_kind(2, 2, 2, 2, 5) == 8
    assert Yatzy.four_of_a_kind(3, 3, 3, 4, 5) == 0


def test_full_house():
    assert Yatzy.fullHouse(2, 2, 3, 3, 3) == 13
    assert Yatzy.fullHouse(4, 4, 4, 5, 5) == 22
    assert Yatzy.fullHouse(2, 2, 3, 4, 5) == 0