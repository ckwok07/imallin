from .Card import Card
from .Rank import Rank
from .Suit import Suit

import random

# A class to represent a standard playing deck with 52 cards.
class Deck:

    # creation of a new deck with 4 differrent suits of each card (2-A).
    def __init__(self) -> None:
        self.cards = []
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(rank, suit))

    # randomly shuffles order of the deck
    def shuffle(self) -> None:
        random.shuffle(self.cards)

    # removes 1 card from the deck and returns it
    def draw(self) -> Card:
        return self.cards.pop()
    
    # removes num cards from the deck and returns them as a list
    def deal(self, num) -> list[Card]:
        output = []
        for i in range(num):
            output.append(self.draw())
        return output
    
    # removes given cards from deck
    def removeCards(self, cards: list[Card]) -> None:
        updated_deck = []

        for card in self.cards:
            remove = False

            for c in cards:
                if card.rank == c.rank and card.suit == c.suit:
                    remove = True
                    break

            if not remove:
                updated_deck.append(card)

        self.cards = updated_deck
