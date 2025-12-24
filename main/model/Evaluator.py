from model.Card import Card


class Evaluator:
    @staticmethod
    def compare_hands(hand1: list[Card], hand2: list[Card]) -> int:

        return 0
    
    @staticmethod
    def best_hand(cards: list[Card]) -> list[Card]:
        return []
    
    @staticmethod
    def mapper(hand: list[Card]) -> tuple[int, int, int, int, int, int]:
        ranks = []
        suits = []

        rankCount = {}

        for card in hand:
            ranks.append(card.rank)
            suits.append(card.suit)

        ranks.sort(Reverse = True)

        for rank in ranks:
            if rank in rankCount:
                rankCount[rank] += 1
            else:
                rankCount[rank] = 1

        # check if straight
        straight = False
        if len(rankCount) == 5:
            # normal straight
            if ranks[-1] - ranks[0] == 4:
                straight = True
                straight_high = ranks[-1]

            # starting with ace
            elif ranks == [2, 3, 4, 5, 14]:
                straight = True
                straight_high = 5


        # check if flush
        flush = False
        if len(set(suits)) == 1:
            flush = True

        # classify hand
        if flush and straight:
            # straight flush
            straightFlush = True
        elif len(rankCount) == 2 and 4 in rankCount.values():
            four = True
        elif len(rankCount) == 2 and 3 in rankCount.valeus() and 2 in rankCount.values():
            boat = True