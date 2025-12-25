from random import random
from main.model.Card import Card
from main.model.Suit import Suit
from main.model.Deck import Deck
from main.model.Evaluator import Evaluator
import random
from itertools import combinations

def test_best_hand_dominates_all_subsets_randomized():
    for _ in range(200):  # number of trials
        deck = Deck()
        deck.shuffle()
        cards = [deck.draw() for _ in range(7)]

        best = Evaluator.best_hand(cards)
        best_score = Evaluator.mapper(best)

        for hand in combinations(cards, 5):
            assert best_score >= Evaluator.mapper(hand)


def test_straight():
    cards = [
        Card(14, Suit.SPADES),
        Card(2, Suit.CLUBS),
        Card(3, Suit.HEARTS),
        Card(4, Suit.SPADES),
        Card(5, Suit.CLUBS),
        Card(14, Suit.DIAMONDS),
        Card(14, Suit.HEARTS)
    ]

    hand = Evaluator.best_hand(cards)
    expected_hand = [Card(14, Suit.SPADES),
                    Card(2, Suit.CLUBS),
                    Card(3, Suit.HEARTS),
                    Card(4, Suit.SPADES),
                    Card(5, Suit.CLUBS)
                ]
    assert Evaluator.mapper(hand) == Evaluator.mapper(expected_hand)
    assert Evaluator.compare_hands(hand,expected_hand) == 0

def test_one_pair():
    cards = [
        Card(9, Suit.SPADES),
        Card(9, Suit.HEARTS),
        Card(14, Suit.CLUBS),
        Card(13, Suit.DIAMONDS),
        Card(11, Suit.SPADES),
        Card(4, Suit.CLUBS),
        Card(2, Suit.HEARTS)
    ]

    hand = Evaluator.best_hand(cards)

    expected_hand = [
        Card(9, Suit.SPADES),
        Card(9, Suit.HEARTS),
        Card(14, Suit.CLUBS),
        Card(13, Suit.DIAMONDS),
        Card(11, Suit.SPADES)
    ]

    assert Evaluator.mapper(hand) == Evaluator.mapper(expected_hand)
    assert Evaluator.compare_hands(hand, expected_hand) == 0

def test_two_pair():
    cards = [
        Card(10, Suit.SPADES),
        Card(10, Suit.HEARTS),
        Card(7, Suit.CLUBS),
        Card(7, Suit.DIAMONDS),
        Card(14, Suit.SPADES),
        Card(4, Suit.HEARTS),
        Card(2, Suit.CLUBS)
    ]

    hand = Evaluator.best_hand(cards)

    expected_hand = [
        Card(10, Suit.SPADES),
        Card(10, Suit.HEARTS),
        Card(7, Suit.CLUBS),
        Card(7, Suit.DIAMONDS),
        Card(14, Suit.SPADES)
    ]

    assert Evaluator.mapper(hand) == Evaluator.mapper(expected_hand)
    assert Evaluator.compare_hands(hand, expected_hand) == 0

def test_three_of_a_kind():
    cards = [
        Card(8, Suit.SPADES),
        Card(8, Suit.HEARTS),
        Card(8, Suit.DIAMONDS),
        Card(14, Suit.CLUBS),
        Card(13, Suit.SPADES),
        Card(4, Suit.CLUBS),
        Card(2, Suit.HEARTS)
    ]

    hand = Evaluator.best_hand(cards)

    expected_hand = [
        Card(8, Suit.SPADES),
        Card(8, Suit.HEARTS),
        Card(8, Suit.DIAMONDS),
        Card(14, Suit.CLUBS),
        Card(13, Suit.SPADES)
    ]

    assert Evaluator.mapper(hand) == Evaluator.mapper(expected_hand)
    assert Evaluator.compare_hands(hand, expected_hand) == 0

def test_full_house():
    cards = [
        Card(6, Suit.SPADES),
        Card(6, Suit.HEARTS),
        Card(6, Suit.DIAMONDS),
        Card(12, Suit.CLUBS),
        Card(12, Suit.SPADES),
        Card(9, Suit.HEARTS),
        Card(2, Suit.CLUBS)
    ]

    hand = Evaluator.best_hand(cards)

    expected_hand = [
        Card(6, Suit.SPADES),
        Card(6, Suit.HEARTS),
        Card(6, Suit.DIAMONDS),
        Card(12, Suit.CLUBS),
        Card(12, Suit.SPADES)
    ]

    assert Evaluator.mapper(hand) == Evaluator.mapper(expected_hand)
    assert Evaluator.compare_hands(hand, expected_hand) == 0

def test_flush():
    cards = [
        Card(14, Suit.HEARTS),
        Card(12, Suit.HEARTS),
        Card(10, Suit.HEARTS),
        Card(8, Suit.HEARTS),
        Card(3, Suit.HEARTS),
        Card(9, Suit.CLUBS),
        Card(2, Suit.SPADES)
    ]

    hand = Evaluator.best_hand(cards)

    expected_hand = [
        Card(14, Suit.HEARTS),
        Card(12, Suit.HEARTS),
        Card(10, Suit.HEARTS),
        Card(8, Suit.HEARTS),
        Card(3, Suit.HEARTS)
    ]

    assert Evaluator.mapper(hand) == Evaluator.mapper(expected_hand)
    assert Evaluator.compare_hands(hand, expected_hand) == 0

def test_straight_flush():
    cards = [
        Card(9, Suit.SPADES),
        Card(10, Suit.SPADES),
        Card(11, Suit.SPADES),
        Card(12, Suit.SPADES),
        Card(13, Suit.SPADES),
        Card(2, Suit.HEARTS),
        Card(4, Suit.CLUBS)
    ]

    hand = Evaluator.best_hand(cards)

    expected_hand = [
        Card(9, Suit.SPADES),
        Card(10, Suit.SPADES),
        Card(11, Suit.SPADES),
        Card(12, Suit.SPADES),
        Card(13, Suit.SPADES)
    ]

    assert Evaluator.mapper(hand) == Evaluator.mapper(expected_hand)
    assert Evaluator.compare_hands(hand, expected_hand) == 0

