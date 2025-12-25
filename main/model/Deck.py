from .Card import Card
from .Rank import Rank
from .Suit import Suit

import random

class Deck:
    def __init__(self) -> None:
        self.cards = []
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(rank, suit))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self) -> Card:
        return self.cards.pop()
    
    def deal(self, num) -> list[Card]:
        hand = []
        for i in range(num):
            hand.append(self.draw())
        return hand
    
    def removeCards(self, card1, card2) -> None:
        updated_deck = []

        for card in self.cards:
            if (card.rank == card1.rank and card.suit == card1.suit):
                continue
            if (card.rank == card2.rank and card.suit == card2.suit):
                continue

            updated_deck.append(card)

        self.cards = updated_deck
