from random import random
from main.model.Card import Card
from main.model.Suit import Suit
from main.model.Deck import Deck
from main.model.Evaluator import Evaluator

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