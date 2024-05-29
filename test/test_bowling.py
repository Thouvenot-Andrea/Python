import pytest

import bowling


# def test_can_create_game():
#     game = bowling.Game()
#
#
# def test_can_roll():
#     game = bowling.Game()
#     game.roll(0)
#
#
# def test_can_score():
#     game = bowling.Game()
#     game.roll(0)
#     score = game.score()
#

# def test_score_is_zero_after_gutter():
#     game = bowling.Game()
#     game.roll(0)
#     score = game.score()
#     assert score == 0

def test_gutter_game():
    game = bowling.Game()
    roll_many(game, 20, 0)
    score = game.score()
    assert score == 0


def test_all_ones():
    game = bowling.Game()
    roll_many(game, 20, 1)
    score = game.score()
    assert score == 20


def roll_many(game, count, value):
    for roll in range(count):
        game.roll(value)


@pytest.mark.skip  # sert a skip le test
def test_one_spare():
    game = bowling.Game()
    game.roll(5)
    game.roll(5)
    game.roll(3)
    roll_many(game, 17, 0)
    score = game.score()
    assert score == 16
