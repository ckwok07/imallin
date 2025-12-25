from .Card import Card
from .Deck import Deck

class Range:
    ALL_HANDS: list[list[Card]] | None = None
    @staticmethod
    def generateHands() -> list[list[Card]]:
        deck = Deck()
        cards = deck.cards
        hands = []

        for i in range(len(cards)):
            for j in range(i + 1, len(cards)):
                hands.append([cards[i], cards[j]])

        return hands


    def __init__(self, hands: list[list[Card]] | None = None) -> None:
        if Range.ALL_HANDS is None:
            Range.ALL_HANDS = Range.generateHands()
        if hands == None:
            self.hands = Range.ALL_HANDS
        else:
            self.hands = hands
