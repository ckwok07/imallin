from main.model.Card import Card
from main.model.Evaluator import Evaluator


def test_high_card():
    hand = [
        Card(14, 'S'),
        Card(13, 'H'),
        Card(11, 'D'),
        Card(9, 'C'),
        Card(2, 'S'),
    ]
    assert Evaluator.mapper(hand) == (0, 14, 13, 11, 9, 2)


def test_high_card_order():
    hand = [
        Card(14, 'H'),
        Card(13, 'D'),
        Card(11, 'C'),
        Card(8, 'S'),
        Card(3, 'H'),
    ]
    assert Evaluator.mapper(hand) == (0, 14, 13, 11, 8, 3)


def test_pair():
    hand = [
        Card(8, 'S'),
        Card(8, 'D'),
        Card(14, 'H'),
        Card(12, 'C'),
        Card(2, 'S'),
    ]
    assert Evaluator.mapper(hand) == (1, 8, 14, 12, 2, 0)


def test_pair_kickers():
    hand = [
        Card(5, 'S'),
        Card(5, 'D'),
        Card(14, 'H'),
        Card(9, 'C'),
        Card(3, 'S'),
    ]
    assert Evaluator.mapper(hand) == (1, 5, 14, 9, 3, 0)


def test_two_pair():
    hand = [
        Card(13, 'S'),
        Card(13, 'D'),
        Card(10, 'H'),
        Card(10, 'C'),
        Card(14, 'S'),
    ]
    assert Evaluator.mapper(hand) == (2, 13, 10, 14, 0, 0)


def test_two_pair_kicker():
    hand = [
        Card(12, 'S'),
        Card(12, 'D'),
        Card(9, 'H'),
        Card(9, 'C'),
        Card(13, 'S'),
    ]
    assert Evaluator.mapper(hand) == (2, 12, 9, 13, 0, 0)


def test_set():
    hand = [
        Card(7, 'S'),
        Card(7, 'D'),
        Card(7, 'H'),
        Card(14, 'C'),
        Card(9, 'S'),
    ]
    assert Evaluator.mapper(hand) == (3, 7, 14, 9, 0, 0)


def test_set_kickers():
    hand = [
        Card(6, 'S'),
        Card(6, 'D'),
        Card(6, 'H'),
        Card(13, 'C'),
        Card(2, 'S'),
    ]
    assert Evaluator.mapper(hand) == (3, 6, 13, 2, 0, 0)


def test_straight():
    hand = [
        Card(9, 'S'),
        Card(8, 'D'),
        Card(7, 'H'),
        Card(6, 'C'),
        Card(5, 'S'),
    ]
    assert Evaluator.mapper(hand) == (4, 9, 0, 0, 0, 0)


def test_wheel_straight():
    hand = [
        Card(14, 'S'),
        Card(2, 'D'),
        Card(3, 'H'),
        Card(4, 'C'),
        Card(5, 'S'),
    ]
    assert Evaluator.mapper(hand) == (4, 5, 0, 0, 0, 0)


def test_flush():
    hand = [
        Card(14, 'S'),
        Card(11, 'S'),
        Card(9, 'S'),
        Card(6, 'S'),
        Card(3, 'S'),
    ]
    assert Evaluator.mapper(hand) == (5, 14, 11, 9, 6, 3)


def test_flush_kickers():
    hand = [
        Card(13, 'H'),
        Card(12, 'H'),
        Card(10, 'H'),
        Card(8, 'H'),
        Card(2, 'H'),
    ]
    assert Evaluator.mapper(hand) == (5, 13, 12, 10, 8, 2)


def test_full_house():
    hand = [
        Card(10, 'S'),
        Card(10, 'D'),
        Card(10, 'H'),
        Card(2, 'C'),
        Card(2, 'S'),
    ]
    assert Evaluator.mapper(hand) == (6, 10, 2, 0, 0, 0)


def test_full_house_order():
    hand = [
        Card(9, 'S'),
        Card(9, 'D'),
        Card(9, 'H'),
        Card(14, 'C'),
        Card(14, 'S'),
    ]
    assert Evaluator.mapper(hand) == (6, 9, 14, 0, 0, 0)


def test_quads():
    hand = [
        Card(8, 'S'),
        Card(8, 'D'),
        Card(8, 'H'),
        Card(8, 'C'),
        Card(14, 'S'),
    ]
    assert Evaluator.mapper(hand) == (7, 8, 14, 0, 0, 0)


def test_quads_kicker():
    hand = [
        Card(5, 'S'),
        Card(5, 'D'),
        Card(5, 'H'),
        Card(5, 'C'),
        Card(2, 'S'),
    ]
    assert Evaluator.mapper(hand) == (7, 5, 2, 0, 0, 0)


def test_straight_flush():
    hand = [
        Card(9, 'S'),
        Card(8, 'S'),
        Card(7, 'S'),
        Card(6, 'S'),
        Card(5, 'S'),
    ]
    assert Evaluator.mapper(hand) == (8, 9, 0, 0, 0, 0)


def test_straight_flush_wheel():
    hand = [
        Card(14, 'H'),
        Card(2, 'H'),
        Card(3, 'H'),
        Card(4, 'H'),
        Card(5, 'H'),
    ]
    assert Evaluator.mapper(hand) == (8, 5, 0, 0, 0, 0)
